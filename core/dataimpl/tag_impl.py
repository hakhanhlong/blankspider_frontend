from ..database.tag import TAGS
from datetime import datetime


def get_bysourceid(sid):
    t = TAGS.objects(source_id=sid)
    return t