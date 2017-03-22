# -*- coding:utf-8 -*-
from flask import render_template, jsonify
from flask.ext.login import login_required

from . import source
from core.dataimpl import tag_impl
from core.dataimpl import content_impl

import json


@source.route('/<sid>/<tagid>', methods=['GET'])
#@login_required
def index(sid, tagid):
    s = tag_impl.get_bysourceid(sid)
    data_master = []


    if tagid != 'all':
        objContents = content_impl.get_bytagid(tagid)
        for x in objContents:
            n_dict = json.loads(x.data)
            data_master.append(n_dict)
            x.data = None

        return render_template('source/index.html', tags=s, contents = objContents, data_masters=data_master)

    else:
        _tagid = str(s[0].id)
        objContents = content_impl.get_bytagid(_tagid)
        for x in objContents:
            n_dict = json.loads(x.data)
            data_master.append(n_dict)
            x.data = None



        #title = test_json['title']
        return render_template('source/index.html', tags=s, contents = objContents, data_masters=data_master)


    return render_template('source/index.html', tags=s)