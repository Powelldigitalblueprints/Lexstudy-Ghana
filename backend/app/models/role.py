from ..extensions import db

user_roles = db.Table(
    "legum_user_roles",
    db.Column("user_id", db.Integer, db.ForeignKey("legum_users.id", ondelete="CASCADE"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey("legum_roles.id", ondelete="CASCADE"), primary_key=True),
)


class Role(db.Model):
    __tablename__ = "legum_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    description = db.Column(db.String(160), nullable=False, default="")

    def __repr__(self):
        return f"<Role {self.name}>"
