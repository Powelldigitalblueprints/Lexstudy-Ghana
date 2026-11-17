from flask import Flask

from .config import Config
from .extensions import db, migrate
from .routes.health import health_bp


def create_app(config_object=None):
    app = Flask(__name__)
    app.config.from_object(config_object or Config)

    if app.config.get("TESTING"):
        app.config["SECRET_KEY"] = app.config.get("SECRET_KEY") or "test-only-secret"
    if not app.config.get("SECRET_KEY"):
        raise RuntimeError("SECRET_KEY must be configured before starting the API.")

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(health_bp, url_prefix="/api/v1")
    return app
