from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    """Report process health, not database readiness."""
    return jsonify(status="ok", service="legum-api", version="0.1.0"), 200
