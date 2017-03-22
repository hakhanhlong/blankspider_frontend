# -*- coding:utf-8 -*-
from flask import render_template
from flask.ext.login import login_required

from . import source
from core.dataimpl import tag_impl
from core.dataimpl import content_impl


@source.route('/<sid>/<tagid>', methods=['GET'])
#@login_required
def index(sid, tagid):
    s = tag_impl.get_bysourceid(sid)



    if tagid != 'all':
        c = content_impl.get_bytagid(tagid)
        return render_template('source/index.html', tags=s, contents = c)

    else:
        _tagid = str(s[0].id)
        c = content_impl.get_bytagid(_tagid)
        return render_template('source/index.html', tags=s, contents = c)


    return render_template('source/index.html', tags=s)