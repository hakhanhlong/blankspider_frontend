# -*- coding:utf-8 -*-
from flask import render_template, jsonify, flash
from flask.ext.login import login_required

from . import repository
from core.dataimpl import tag_impl
from core.dataimpl import content_impl
from core.dataimpl import source_impl
import json

from flask_moment import Moment

from datetime import datetime

from core.api.request_helpers import RequestHelpers
from core.api.request_url import RequestURL

@repository.route('/', methods=['GET'])
def index():
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
                    timing['published_at'] = datetime.strptime(timing['published_at'].replace('T00:00:00.000Z', ''),'%Y-%m-%d')
                except:
                    break
            x.timings = timings
        # ------------------------------------------------------------------------------------------------------------------
    except Exception as ex:
        flash('ERROR:' + ex, 'danger')


    return render_template('repository/index.html', sources = sources)

@repository.route('/detail/<cid>', methods=['GET'])
def detail(cid):
    cont = content_impl.get_byid(cid)
    #n_dict = json.loads(cont.data)
    data_master = []

    try:
        for item in cont.data:
            for k, v in item.items():
                data_master.append({'key': k, 'value': json.loads(v)})
    except Exception as ex:
        flash('ERROR:' + ex.message, 'danger')


    return render_template('repository/detail.html', data=data_master, link_href = cont.href, contentid=cid)

@repository.route('/detail-html/<cid>/<idx>', methods=['GET'])
def detail_html(cid, idx):
    cont = content_impl.get_byid(cid)
    #n_dict = json.loads(cont.data)
    data_master = []
    try:
        for k, v in cont.data[int(idx)].items():
            data_master.append({'key': k, 'value': json.loads(v)})
    except Exception as ex:
        flash('ERROR:' + ex.message, 'danger')

    #cont.data = None

    #return data_master[0]['value']['html_data'].replace("document.domain", "")
    return render_template('repository/detail_html.html', data=data_master[0]['value']['html_data'].replace("document.domain", ""))