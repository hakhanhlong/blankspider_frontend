from ..database.content_img import CONTENT_IMG

def getByContentId(cid = ''):
    imgs = CONTENT_IMG.objects(content_id = cid)
    return imgs
