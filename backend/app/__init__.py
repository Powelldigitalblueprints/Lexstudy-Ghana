from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from .config import Config
from .extensions import db, limiter, migrate
from .routes.auth import auth_bp
from .routes.health import health_bp
from .security import csrf_protect


def create_app(config_object=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if isinstance(config_object, dict):
        app.config.update(config_object)
    elif config_object is not None:
        app.config.from_object(config_object)

    if app.config.get("TESTING"):
        app.config["SECRET_KEY"] = app.config.get("SECRET_KEY") or "test-only-secret"
    if not app.config.get("SECRET_KEY"):
        raise RuntimeError("SECRET_KEY must be configured before starting the API.")

    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)
    csrf_protect(app)

    from . import models  # noqa: F401

    @app.after_request
    def add_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        return response

    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        return jsonify(error={
            "code": error.name.lower().replace(" ", "_"),
            "message": error.description,
        }), error.code

    @app.errorhandler(429)
    def handle_rate_limit(error):
        return jsonify(error={
            "code": "rate_limit_exceeded",
            "message": "Too many requests. Please try again later.",
        }), 429

    app.register_blueprint(health_bp, url_prefix="/api/v1")
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    return app
