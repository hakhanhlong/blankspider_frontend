from app import db


class TAGS(db.Document):
    source_id = db.StringField(max_length=255)
    name = db.StringField(max_length=255)
    count = db.IntField()
    __v = db.IntField()

    meta = {"db_alias": "lcbc_content_archived", 'collection': 'tags', 'strict': False}

