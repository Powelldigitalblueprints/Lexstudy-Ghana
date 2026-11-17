import secrets
from functools import wraps

from flask import jsonify, request, session

from .extensions import db
from .models import User


SAFE_METHODS = {"GET", "HEAD", "OPTIONS"}


def issue_csrf_token():
    token = secrets.token_urlsafe(32)
    session["csrf_token"] = token
    return token


def csrf_protect(app):
    @app.before_request
    def verify_csrf_token():
        if request.method in SAFE_METHODS:
            return None
        expected = session.get("csrf_token")
        supplied = request.headers.get("X-CSRF-Token", "")
        if not expected or not supplied or not secrets.compare_digest(expected, supplied):
            return jsonify(error={"code": "csrf_failed", "message": "A valid CSRF token is required."}), 403
        return None


def get_current_user():
    user_id = session.get("user_id")
    if user_id is None:
        return None
    return db.session.get(User, user_id)


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        user = get_current_user()
        if user is None or not user.is_active:
            return jsonify(error={"code": "authentication_required", "message": "Please sign in to continue."}), 401
        return view(*args, **kwargs)
    return wrapped
