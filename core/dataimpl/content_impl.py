from ..database.content import CONTENTS
from datetime import datetime

def get_bytagid(sid):
    t = CONTENTS.objects(tag_id = str(sid)).no_cache()[:50]
    #t = CONTENTS.objects()[:50]
    return t

def get_byid(cid):
    ac = CONTENTS.objects.get_or_404(id=cid)
    return ac