from app import db
from datetime import datetime

class CONTENT_IMG(db.Document):
    content_id = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now)
    images = db.ListField()
    __v = db.IntField()
    meta = {"db_alias": "blankspider_content_archived", 'collection': 'contentstorages', 'strict': False}