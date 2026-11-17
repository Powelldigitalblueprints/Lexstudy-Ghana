from flask import Blueprint, current_app, jsonify
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from ..extensions import db

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    """Liveness check. Does not depend on database availability."""
    return jsonify(status="ok", service="legum-api", version="0.1.0"), 200


@health_bp.get("/ready")
def ready():
    """Readiness check including a lightweight database connectivity test."""
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify(status="ready", service="legum-api"), 200
    except SQLAlchemyError:
        db.session.rollback()
        current_app.logger.exception("Database readiness check failed")
        return jsonify(status="unavailable", service="legum-api"), 503
