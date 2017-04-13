# -*- coding:utf-8 -*-
from flask import render_template, json
from flask import jsonify
from . import ajax

from core.api.services.tag_service import TagService




@ajax.route('/tag_get_by_source/<sid>', methods=['GET'])
def tag_get_by_source(sid):
    tag_service = TagService()
    return jsonify(tag_service.get_by_source(sid))