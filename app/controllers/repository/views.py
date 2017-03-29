# -*- coding:utf-8 -*-
from flask import render_template, jsonify
from flask.ext.login import login_required

from . import repository
from core.dataimpl import tag_impl
from core.dataimpl import content_impl
from core.dataimpl import source_impl

@repository.route('/', methods=['GET'])
def index():
    sources = source_impl.get_all_active(True)
    for x in sources:
        x.tags = tag_impl.get_bysourceid(str(x.id))

    return render_template('repository/index.html', sources = sources)