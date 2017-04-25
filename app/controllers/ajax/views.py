# -*- coding:utf-8 -*-
from flask import render_template, json
from flask import jsonify
from . import ajax

from core.api.services.tag_service import TagService
from core.api.services.content_service import ContentService
from core.control.pagination import Pagination





@ajax.route('/tag/get_by_source/<sid>', methods=['GET'])
def tag_get_by_source(sid):
    tag_service = TagService()
    return jsonify(tag_service.get_by_source(sid))


@ajax.route('/content/filter_by_ptiming/<sid>/<ptimingid>/', methods=['GET'])
@ajax.route('/content/filter_by_ptiming/<sid>/<ptimingid>/<page>', methods=['GET'])
def content_filter_by_timing(sid, ptimingid, page=1):
    content_service = ContentService()
    content = content_service.filter_by_timing(sid, ptimingid, int(page), 20)
    count_items = content['message']['total']
    pagination = Pagination(int(page), 20, count_items)

    data_master = []
    for item in content['message']['docs']:
        item['number_version'] = len(item['data'])
        item['published_at_text'] = (json.loads(item['data'][0]['1']))['published_at']
        del item['data']
        data_master.append(item)
    return render_template('ajax/filter_by_ptiming.html', contents=data_master, pagination = pagination,
                           params={'sid':sid, 'ptimingid':ptimingid})

    #return jsonify(content)


@ajax.route('/content/list_by_default/', methods=['GET'])
@ajax.route('/content/list_by_default/<page>', methods=['GET'])
def content_list_by_default(page=1):
    content_service = ContentService()
    content = content_service.list_by_default(int(page), 20)
    count_items = content['message']['total']
    pagination = Pagination(int(page), 20, count_items)

    data_master = []
    for item in content['message']['docs']:
        item['number_version'] = len(item['data'])
        item['published_at_text'] = (json.loads(item['data'][0]['1']))['published_at']
        del item['data']
        data_master.append(item)
    return render_template('ajax/list_by_default.html', contents=data_master, pagination = pagination)