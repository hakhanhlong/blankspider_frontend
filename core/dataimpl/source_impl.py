from ..database.source import SOURCES
from datetime import datetime



def get_all():
    s = SOURCES.objects()
    return s

def get_all_active(isactive = True):
    s = SOURCES.objects(is_active=isactive)
    return s

def get_by_id(sid):
    s = SOURCES.objects(id=sid).first()
    return s

def get_by_projectid(pid):
    s = SOURCES.objects(project_id=str(pid))
    return s


def insert(name, mode,is_active,status,created_by,project_id,project_name, type):
    s = SOURCES(name=name, mode=mode, is_active=is_active, status=status, created_by=created_by, project_id=project_id, project_name=project_name, type_spider=type)
    return s.save()

def update(id, name, mode, is_active, status, project_id, project_name, type=type):
    s = SOURCES.objects(id=id).first()
    s.name = name
    s.mode = mode
    s.is_active = is_active
    s.status = status
    s.project_id = project_id
    s.project_name = project_name
    s.type_spider=type
    return s.save()