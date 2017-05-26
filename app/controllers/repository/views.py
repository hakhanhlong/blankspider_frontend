# -*- coding:utf-8 -*-
from flask import render_template, jsonify, flash
from flask.ext.login import login_required

from core.api.services.content_service import ContentService
from . import repository
from core.dataimpl import tag_impl
from core.dataimpl import content_impl
from core.dataimpl import source_impl
import json

from flask_moment import Moment

from datetime import datetime

from core.api.request_helpers import RequestHelpers
from core.api.request_url import RequestURL
from core.control.pagination import Pagination

PAGE_DETAIL = 2  # previous page =2 = pagedetail.html
PAGE_FILTER_DEFAULT = 0  # previous page = 0 = index2.html
PAGE_FILTER_BY_TIMING = 1  # previous page = 1 = datatable.html(inside index2)


def get_data_from_service_filter_by_default(page=0):
    content_service = ContentService()
    content = content_service.list_by_default(int(page), 50)
    count_items = content['response']['numFound']
    pagination = Pagination(int(page), 50, count_items)
    data_master = []
    for item in content['response']['docs']:
        data_master.append(item)
    aDict = {}
    aDict['items'] = data_master
    aDict['pagingnation'] = pagination;
    return aDict;


def get_data_from_service_filter_by_timing(sid, ptimingid, page=0):
    content_service = ContentService()
    content = content_service.filter_by_timing(sid, ptimingid, int(page), 50)
    count_items = content['response']['numFound']
    pagination = Pagination(int(page), 50, count_items)
    data_master = []
    for item in content['response']['docs']:
        data_master.append(item)
    aDict = {}
    aDict['items'] = data_master
    aDict['pagingnation'] = pagination;
    return aDict


def get_source():
    sources = source_impl.get_all_active(True)
    _request = RequestHelpers()
    _requestURL = RequestURL()
    _request.url = _requestURL.PUBLISHTIMING_URL_LISTBYSOURCE

    try:
        # fill data timing to source
        for x in sources:
            _request.params = {'source_id': str(x.id), 'limit': 10}
            timings = _request.post_json().json()
            for timing in timings:
                try:
                    timing['published_at'] = datetime.strptime(timing['published_at'].replace('T00:00:00.000Z', ''),
                                                               '%Y-%m-%d')
                except:
                    break
            x.timings = timings
            # ------------------------------------------------------------------------------------------------------------------
    except Exception as ex:
        flash('ERROR:' + ex, 'danger')
    return sources


@repository.route('/filter-by-timing/<sid>/<ptimingid>/', methods=['GET'])
@repository.route('/filter-by-timing/<sid>/<ptimingid>/<page>', methods=['GET'])
@repository.route('/filter-by-timing/<sid>/<ptimingid>/<page>/<pageid>', methods=['GET'])
def content_filter_by_timing(sid, ptimingid, page=0, pageid=-1):
    aDict = get_data_from_service_filter_by_timing(sid, ptimingid, page)
    print("items = " + str(len(aDict['items'])))
    if int(pageid) != PAGE_DETAIL:
        return render_template('/data_table.html', contents=aDict['items'], pagination=aDict['pagingnation'],
                               params={'sid': sid, 'ptimingid': ptimingid, 'pageid': PAGE_FILTER_BY_TIMING})
    else:
        return render_template('repository/index2.html', sources=get_source(), contents=aDict['items'],
                               pagination=aDict['pagingnation'], params={'pageid': PAGE_FILTER_DEFAULT})


@repository.route('/', methods=['GET'])
@repository.route('/<page>', methods=['GET'])
@repository.route('/<page>/<pageid>', methods=['GET'])
def index(page=0, pageid=0):
    sources = get_source()
    aDict = get_data_from_service_filter_by_default(page)
    print("page = " + str(page) + "pageid = " + str(pageid))
    if pageid == int(PAGE_FILTER_DEFAULT) and int(page) == 0:
        return render_template('repository/index2.html', sources=sources, contents=aDict['items'],
                               pagination=aDict['pagingnation'], params={'pageid': PAGE_FILTER_DEFAULT})
    elif pageid == PAGE_DETAIL:
        return render_template('repository/index2.html', sources=sources, contents=aDict['items'],
                               pagination=aDict['pagingnation'], params={'pageid': PAGE_FILTER_DEFAULT})
    elif pageid == PAGE_FILTER_DEFAULT and int(page) > 0:
        return render_template('/data_table.html', sources=sources, contents=aDict['items'],
                               pagination=aDict['pagingnation'], params={'pageid': PAGE_FILTER_DEFAULT})


@repository.route('/detail/<cid>', methods=['GET'])
@repository.route('/detail/<cid>/<page>', methods=['GET'])
@repository.route('/detail/<cid>/<page>/<prepageid>', methods=['GET'])
@repository.route('/detail/<cid>/<page>/<prepageid>/<sid>', methods=['GET'])
def detail(cid, page=0, prepageid=0, sid=0):
    print("cid = " + cid)
    cont = content_impl.get_byid(cid)
    # n_dict = json.loads(cont.data)
    data_master = []

    try:
        for item in cont.data:
            for k, v in item.items():
                data_master.append({'key': k, 'value': json.loads(v)})
                print("key = " + k + "value = " + v)
    except Exception as ex:
        flash('ERROR:' + ex.message, 'danger')
    return render_template('repository/pagedetail.html', sources=get_source(), data=data_master, link_href=cont.href,
                           contentid=cid,
                           params={'pageid': PAGE_DETAIL, 'page': page, 'prepageid': prepageid, 'sid': sid})


@repository.route('/detail-iframe/<cid>/<idx>', methods=['GET'])
def detail_iframe(cid, idx):
    print("cid = " + cid)
    cont = content_impl.get_byid(cid)
    # n_dict = json.loads(cont.data)
    data_master = []

    try:
        for item in cont.data:
            for k, v in item.items():
                data_master.append({'key': k, 'value': json.loads(v)})
                print("key = " + k + "value = " + v)
    except Exception as ex:
        flash('ERROR:' + ex.message, 'danger')
    return render_template('repository/detailiframe.html', sources=get_source(), data=data_master, link_href=cont.href,
                           contentid=cid, index=idx)


@repository.route('/detail-html/<cid>/<idx>', methods=['GET'])
def detail_html(cid, idx):
    cont = content_impl.get_byid(cid)
    # n_dict = json.loads(cont.data)
    data_master = []
    try:
        for k, v in cont.data[int(idx)].items():
            data_master.append({'key': k, 'value': json.loads(v)})
    except Exception as ex:
        flash('ERROR:' + ex.message, 'danger')

    # cont.data = None

    # return data_master[0]['value']['html_data'].replace("document.domain", "")
    return render_template('repository/detail_html.html',
                           data=data_master[0]['value']['html_data'].replace("document.domain", ""))
