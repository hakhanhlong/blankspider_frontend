from ..database.content import CONTENTS
from datetime import datetime

def get_bytagid(sid):
    t = CONTENTS.objects(tag_id = str(sid)).order_by('-created_at').no_cache()[:100]
    #t = CONTENTS.objects()[:50]
    return t

def get_byid(cid):
    ac = CONTENTS.objects.get_or_404(id=cid)
    return ac