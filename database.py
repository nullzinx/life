
from setup import db
from datetime import datetime, timezone

class Habits(db.Model):
    __tablename__ = "habits"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    virtue = db.Column(db.Boolean)  
    started_sequencie = db.Column(db.DateTime(timezone=True)) 


class Wish_list(db.Model):
    __tablename__ = "wishlist"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(500))
    action_plain = db.Column(db.String(3000))


class mark_datas(db.Model):
    __tablename__ = "markdatas" 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    notify_at = db.Column(db.DateTime(timezone=True))


class Diary(db.Model):
    __tablename__ = "diary"
    id = db.Column(db.Integer, primary_key=True)
    encrypted_token = db.Column(db.String(128))
    anoted_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    anoted_encrypt_title = db.Column(db.String(300))
    anoted_encrypt_content = db.Column(db.String(1000))
    salt = db.Column(db.String(16))

