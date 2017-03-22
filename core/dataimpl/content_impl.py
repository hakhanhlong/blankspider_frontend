from ..database.content import CONTENTS
from datetime import datetime

def get_bytagid(sid):
    t = CONTENTS.objects(tag_id = str(sid)).no_cache()
    #t = CONTENTS.objects()[:50]
    return t