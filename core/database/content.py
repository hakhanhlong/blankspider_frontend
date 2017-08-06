from app import db
from datetime import datetime


class CONTENTS(db.Document):
    source_id = db.StringField(max_length=255)
    href = db.StringField(max_length=255)
    tag_name = db.StringField(max_length=255)
    data=db.DictField()
    version = db.StringField(max_length=255)
    href_md5 = db.StringField(max_length=255)
    tag_id = db.StringField(max_length=255)
    created_at = db.DateTimeField(default=datetime.now)
    content_hash = db.StringField(max_length=255)
    __v = db.IntField()
    content_img = None
    meta = {"db_alias": "blankspider_content_archived", 'collection': 'contents', 'strict': False}
