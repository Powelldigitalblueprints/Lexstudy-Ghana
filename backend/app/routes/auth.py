import re

from flask import Blueprint, jsonify, request, session

from ..extensions import db, limiter
from ..models import AuditLog, Role, User
from ..security import get_current_user, issue_csrf_token, login_required

auth_bp = Blueprint("auth", __name__)
EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def _payload():
    return request.get_json(silent=True) or {}


def _audit(event_type, user_id=None):
    db.session.add(AuditLog(
        user_id=user_id,
        event_type=event_type,
        ip_address=request.remote_addr,
    ))


@auth_bp.get("/csrf")
def csrf_token():
    return jsonify(csrf_token=issue_csrf_token()), 200


@auth_bp.post("/register")
@limiter.limit("5 per hour")
def register():
    data = _payload()
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip().lower()
    password = data.get("password", "")

    if not name or len(name) > 120:
        return jsonify(error={"code": "invalid_name", "message": "Enter a name of up to 120 characters."}), 400
    if len(email) > 254 or not EMAIL_PATTERN.match(email):
        return jsonify(error={"code": "invalid_email", "message": "Enter a valid email address."}), 400
    if not isinstance(password, str) or len(password) < 12 or len(password) > 128:
        return jsonify(error={"code": "weak_password", "message": "Password must contain between 12 and 128 characters."}), 400
    if User.query.filter_by(email=email).first():
        return jsonify(error={"code": "account_exists", "message": "An account with that email already exists."}), 409

    student_role = Role.query.filter_by(name="student").first()
    if student_role is None:
        student_role = Role(name="student", description="Standard student account")
        db.session.add(student_role)
        db.session.flush()

    user = User(name=name, email=email)
    user.set_password(password)
    user.roles.append(student_role)
    db.session.add(user)
    db.session.flush()
    _audit("account.registered", user.id)
    db.session.commit()

    session.clear()
    session["user_id"] = user.id
    session.permanent = True
    token = issue_csrf_token()
    return jsonify(user=user.public_dict(), csrf_token=token), 201


@auth_bp.post("/login")
@limiter.limit("5 per minute")
def login():
    data = _payload()
    email = str(data.get("email", "")).strip().lower()
    password = data.get("password", "")
    user = User.query.filter_by(email=email).first() if email else None

    if user is None or not user.is_active or not isinstance(password, str) or len(password) > 128 or not user.check_password(password):
        return jsonify(error={"code": "invalid_credentials", "message": "Email or password is incorrect."}), 401

    session.clear()
    session["user_id"] = user.id
    session.permanent = True
    _audit("account.login", user.id)
    db.session.commit()
    token = issue_csrf_token()
    return jsonify(user=user.public_dict(), csrf_token=token), 200


@auth_bp.post("/logout")
@login_required
def logout():
    user = get_current_user()
    _audit("account.logout", user.id)
    db.session.commit()
    session.clear()
    return jsonify(message="You have been signed out."), 200


@auth_bp.get("/me")
@login_required
def me():
    return jsonify(user=get_current_user().public_dict()), 200
