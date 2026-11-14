"""Premium Claude tutor routes for LexStudy Ghana."""
import os
from datetime import date
from flask import jsonify, render_template, request, session
from anthropic import Anthropic

MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-5")
DAILY_LIMIT = max(1, int(os.getenv("CLAUDE_LEGUM_DAILY_LIMIT", "25")))
SYSTEM_PROMPT = """You are the premium AI study tutor for LexStudy Ghana, a Ghanaian legal
studies platform. Help law students understand legal concepts, structure IRAC answers,
analyse hypothetical facts and revise course materials. Prioritise Ghana's 1992
Constitution and Ghanaian legislation and authorities when relevant. Do not invent
case names, citations, statutory provisions, quotations or holdings. If you cannot
verify an authority from the supplied context or reliable knowledge, say so and ask
the student to check the reported judgment or current legislation. Clearly distinguish
hypothetical practice facts from real cases. Explain that your answer is educational
and not legal advice. Never present a generated answer as a verified court judgment."""
_client = None

def _claude_client():
    global _client
    if _client is None:
        key = os.getenv("ANTHROPIC_API_KEY", "").strip()
        if not key:
            raise RuntimeError("ANTHROPIC_API_KEY is not configured")
        _client = Anthropic(api_key=key, timeout=45.0, max_retries=1)
    return _client

def register_claude_routes(app, login_required, current_user, user_is_pro, connect):
    @app.get("/ai")
    @login_required
    def claude_tutor_page():
        user = current_user()
        if not user or not user_is_pro(user["id"]):
            return render_template("ai_tutor.html", premium_required=True), 403
        enabled = os.getenv("CLAUDE_ENABLED", "false").strip().lower() == "true"
        return render_template("ai_tutor.html", premium_required=False, enabled=enabled)

    @app.post("/api/ai/chat")
    @login_required
    def claude_tutor_chat():
        user = current_user()
        if not user or not user_is_pro(user["id"]):
            return jsonify({"error": "A premium subscription is required to use the AI tutor."}), 403
        if os.getenv("CLAUDE_ENABLED", "false").strip().lower() != "true":
            return jsonify({"error": "The AI tutor is temporarily unavailable."}), 503
        payload = request.get_json(silent=True) or {}
        question = str(payload.get("message", "")).strip()
        history = payload.get("history", [])
        if not question or len(question) > 5000:
            return jsonify({"error": "Enter a question of no more than 5,000 characters."}), 400
        if not isinstance(history, list):
            history = []
        messages = []
        for item in history[-8:]:
            if not isinstance(item, dict) or item.get("role") not in ("user", "assistant"):
                continue
            content = str(item.get("content", "")).strip()
            if content and len(content) <= 5000:
                messages.append({"role": item["role"], "content": content})
        messages.append({"role": "user", "content": question})
        today = date.today().isoformat()
        conn = connect()
        try:
            conn.execute("""CREATE TABLE IF NOT EXISTS claude_ai_daily_usage (
                user_id INTEGER NOT NULL, usage_date TEXT NOT NULL,
                request_count INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (user_id, usage_date))""")
            reserved = conn.execute("""INSERT INTO claude_ai_daily_usage(user_id, usage_date, request_count)
                VALUES (?, ?, 1)
                ON CONFLICT(user_id, usage_date) DO UPDATE
                SET request_count = claude_ai_daily_usage.request_count + 1
                WHERE claude_ai_daily_usage.request_count < ?
                RETURNING request_count""",
                (user["id"], today, DAILY_LIMIT)).fetchone()
            conn.commit()
            if not reserved:
                return jsonify({"error": f"You have reached today's limit of {DAILY_LIMIT} AI questions."}), 429
        finally:
            conn.close()
        try:
            result = _claude_client().messages.create(
                model=MODEL, max_tokens=1400, system=SYSTEM_PROMPT, messages=messages
            )
            answer = "\n".join(block.text for block in result.content if block.type == "text").strip()
            return jsonify({"answer": answer or "I could not prepare an answer. Please try again."})
        except Exception as exc:
            app.logger.warning("Claude tutor request failed: %s", type(exc).__name__)
            return jsonify({"error": "The AI tutor could not respond just now. Please try again."}), 502
