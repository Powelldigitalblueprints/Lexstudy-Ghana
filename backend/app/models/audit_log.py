from datetime import datetime, timezone

from ..extensions import db


class AuditLog(db.Model):
    __tablename__ = "legum_audit_logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("legum_users.id", ondelete="SET NULL"), nullable=True, index=True)
    event_type = db.Column(db.String(80), nullable=False, index=True)
    ip_address = db.Column(db.String(45), nullable=True)
    details = db.Column(db.JSON, nullable=False, default=dict)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
