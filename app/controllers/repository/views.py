# -*- coding:utf-8 -*-
from flask import render_template, jsonify, flash, session
from flask.ext.login import login_required

from core.api.services.content_service import ContentService

import core.api.services.tag_service
from . import repository
from core.dataimpl import tag_impl, content_img_impl
from core.dataimpl import content_impl
from core.dataimpl import source_impl
from core.dataimpl import configuration_impl
import json

from flask_moment import Moment

from datetime import datetime

from core.api.request_helpers import RequestHelpers
from core.api.request_url import RequestURL
from core.control.pagination import Pagination

from lxml import html, etree
from io import StringIO, BytesIO
import re

PAGE_DETAIL = 2  # previous page =2 = pagedetail.html
PAGE_FILTER_DEFAULT = 0  # previous page = 0 = index2.html
PAGE_FILTER_BY_TIMING = 1  # previous page = 1 = datatable.html(inside index2)
PAGE_SEARCH = 3
PAGE_REPORT_SOURCE = 4;
PAGE_REPORT_TAG = 5;
IMAGE_URL = "http://img.lcbc.digicomdemo.vn/"
userNameDefault = "admin"
passwordDefault = "admin"


def get_data_from_service_filter_by_default(page=0):
    content_service = ContentService()
    content = content_service.list_by_default(int(page), 50)
    count_items = content['response']['numFound']
    p = int(page)
    if p == 0:
        p = 1
    pagination = Pagination(p, 50, count_items)
    data_master = []
    for item in content['response']['docs']:
        try:
            item['source_name'] = source_impl.get_by_id(item['source_id']).name
        except Exception as ex:
            print("exception : " + str(ex))
        data_master.append(item)
    aDict = {}
    aDict['items'] = data_master
    aDict['pagingnation'] = pagination;
    return aDict;


def get_data_from_service_filter_by_timing(sid, ptimingid, page=0):
    try:
        content_service = ContentService()
        content = content_service.filter_by_timing(sid, ptimingid, int(page), 50)
        count_items = content['response']['numFound']
        p = int(page)
        if p == 0:
            p = 1
        pagination = Pagination(p, 50, count_items)
        data_master = []
        for item in content['response']['docs']:
            try:
                item['source_name'] = source_impl.get_by_id(item['source_id']).name
            except Exception as ex:
                print("exception : " + str(ex))
            data_master.append(item)
        aDict = {}
        aDict['items'] = data_master
        aDict['pagingnation'] = pagination;
        return aDict
    except Exception as ex:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"+str(ex))
        return None


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
        print('xxxxxxxxxxxxxxxxxxxxxxxxxx' + str(ex))
        flash('ERROR:' + str(ex), 'danger')
    return sources


@repository.route('/filter-by-timing/<sid>/<ptimingid>/', methods=['GET'])
@repository.route('/filter-by-timing/<sid>/<ptimingid>/<page>', methods=['GET'])
@repository.route('/filter-by-timing/<sid>/<ptimingid>/<page>/<pageid>', methods=['GET'])
def content_filter_by_timing(sid, ptimingid, page=0, pageid=-1):
    aDict = get_data_from_service_filter_by_timing(sid, ptimingid, page)
    if int(pageid) != PAGE_DETAIL:
        return render_template('/data_table.html', contents=aDict['items'], pagination=aDict['pagingnation'],
                               params={'sid': sid, 'ptimingid': ptimingid, 'pageid': PAGE_FILTER_BY_TIMING})
    else:
        return render_template('repository/index2.html', sources=get_source(), contents=aDict['items'],
                               pagination=aDict['pagingnation'],
                               params={'sid': sid, 'ptimingid': ptimingid, 'pageid': PAGE_FILTER_BY_TIMING})


@repository.route('/', methods=['GET'])
@repository.route('/<page>', methods=['GET'])
@repository.route('/<page>/<pageid>', methods=['GET'])
def index(page=0, pageid=0):
    # session['logged_in'] = False
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        sources = get_source()
        # for item in sources:
        #     print("name = "+str(item.name))
        #     print("created_date = "+str(item.created_date))
        #     tag_service = TagService()
        #     tags = tag_service.get_by_source(str(item.id))
        #     print(len(tags))
        #     for i in tags:
        #         print("count i ="+str(i))
        aDict = get_data_from_service_filter_by_default(page)
        if pageid == int(PAGE_FILTER_DEFAULT) and int(page) == 0:
            return render_template('repository/index2.html', sources=sources, contents=aDict['items'],
                                   pagination=aDict['pagingnation'], params={'pageid': PAGE_FILTER_DEFAULT})
        elif pageid == PAGE_DETAIL:
            return render_template('repository/index2.html', sources=sources, contents=aDict['items'],
                                   pagination=aDict['pagingnation'], params={'pageid': PAGE_FILTER_DEFAULT})
        elif pageid == PAGE_FILTER_DEFAULT and int(page) > 0:
            return render_template('/data_table.html', sources=sources, contents=aDict['items'],
                                   pagination=aDict['pagingnation'], params={'pageid': PAGE_FILTER_DEFAULT})


@repository.route('/login/<username>/<password>', methods=['POST'])
def login(username="", password=""):
    if username == userNameDefault and password == passwordDefault:
        session['logged_in'] = True
        return "1"
    else:
        return render_template("login.html")


@repository.route('/detail/<cid>/', methods=['GET'])
@repository.route('/detail/<cid>/<page>/', methods=['GET'])
@repository.route('/detail/<cid>/<page>/<prepageid>/', methods=['GET'])
@repository.route('/detail/<cid>/<page>/<prepageid>/<ptimingid>/', methods=['GET'])
def detail(cid, page=0, prepageid=0, ptimingid=0):
    kw = '*'
    if not session.get('logged_in'):
        return render_template("login.html")
    cont = content_impl.get_byid(cid)
    s = source_impl.get_by_id(cont.source_id)
    content_im = content_img_impl.getByContentId(cid)
    data_master = []

    try:
        i = 0;
        for item in cont.data:
            for k, v in item.items():
                _val = json.loads(v)
                if content_im is not None and len(content_im[0].images) > 0:
                    directory1, directory2, directory3, directory4, directory5, directory6, imageName = \
                        content_im[0].images[i]['image_full_content'].split("/")
                    directory7, directory8, directory9, directory10, directory11, directory12, imageName1 = \
                        content_im[0].images[i]['image_filter_content'].split("/")
                    _val['image_full_content'] = directory6 + "-" + imageName
                    _val['image_filter_content'] = directory12 + "-" + imageName1
                    i = i + 1;
                data_master.append({'key': k, 'value': _val})

    except Exception as ex:
        pass
    pagination = Pagination(int(1), 1, len(data_master))
    return render_template('repository/pagedetail.html', sources=get_source(), data=data_master, link_href=cont.href,
                           contentid=cid, pagination=pagination, source=s,
                           params={'pageid': PAGE_DETAIL, 'page': page, 'prepageid': prepageid,
                                   'ptimingid': ptimingid,'kw': kw})


@repository.route('/detail_html/<cid>/<idx>/<pdfurl>', methods=['GET'])
def detail_html(cid, idx, pdfurl):
    if not session.get('logged_in'):
        return render_template("login.html")
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
    return render_template('viewer.html',
                           data=data_master[0]['value']['html_data'].replace("document.domain", ""))


@repository.route('/display_pdf/<pdfurl>/<kw>/<scale>', methods=['GET'])
def display_pdf(pdfurl="", kw="",scale=""):
    if not session.get('logged_in'):
        return render_template("login.html")
    pdfurl = IMAGE_URL + pdfurl.replace("-", "/")
    return render_template('viewer.html', pdfdocument=pdfurl, kw=kw, scale=scale)


@repository.route('/search/', methods=['GET'])
@repository.route('/search/<source>/<tag>/<published_from>/<published_to>/<kw>/<page>', methods=['GET'])
def content_search(source='', tag='', published_from='', published_to='', kw='', page=0):
    if not session.get('logged_in'):
        return render_template("login.html")
    content_service = ContentService()

    if published_from != '*':
        if 'T00:00:00.000Z' not in published_from:
            published_from = published_from.replace('T00:00:00.000Z', '')
            published_from = published_from.split('-')[::-1]
            published_from = '-'.join(published_from) + 'T00:00:00.000Z'

    if published_to  != '*':
        if 'T00:00:00.000Z' not in published_to:
            published_to = published_to.replace('T00:00:00.000Z', '')
            published_to = published_to.split('-')[::-1]
            published_to = '-'.join(published_to) + 'T00:00:00.000Z'

    content = content_service.search(source, tag, published_from, published_to, kw, int(page), 50)
    count_items = content['response']['numFound']
    p = int(page)
    if p == 0:
        p = 1
    pagination = Pagination(p, 50, count_items)
    data_master = []
    for item in content['response']['docs']:
        try:
            item['source_name'] = source_impl.get_by_id(item['source_id']).name
        except Exception as ex:
            print("exception : " + str(ex))
        data_master.append(item)
    return render_template('/data_table.html', contents=data_master, pagination=pagination,
                           params={'source': source, 'tag': tag, 'published_from': published_from,
                                   'published_to': published_to, 'kw': kw, 'page': page,
                                   'pageid': PAGE_SEARCH})


@repository.route('/search_to_detail/<cid>/<source>/<tag>/<published_from>/<published_to>/<kw>/<page>', methods=['GET'])
def search_to_detail(cid, source, tag, published_from, published_to, kw, page):
    if not session.get('logged_in'):
        return render_template("login.html")
    if published_from != '*':
        year, month, day = published_from.split("-")
        published_from = day + "-" + month + "-" + year
    if published_to != '*':
        year, month, day = published_to.split("-")
        published_to = day + "-" + month + "-" + year
    cont = content_impl.get_byid(cid)
    s = source_impl.get_by_id(cont.source_id)
    content_im = content_img_impl.getByContentId(cid)
    configuration = configuration_impl.get_config('SOURCE', cont.source_id)
    # n_dict = json.loads(cont.data)
    data_master = []

    try:
        for item in cont.data:
            i = 0
            for k, v in item.items():

                _val = json.loads(v)
                content = _val['content']
                try:
                    if configuration['config']['PARSERVIDEOS']:
                        configs = configuration['config']['PARSERVIDEOS']['data']
                        array_player = []
                        array_embeded_player = []
                        array_player_id = []
                        htmlparser = etree.HTMLParser(recover=True, remove_blank_text=True)
                        # tree = etree.parse(StringIO(content), htmlparser)
                        tree = etree.fromstring(str(content), htmlparser)

                        attribute = configs['attribute']
                        attribute_pattern_value = attribute['step']['1']['field_value']

                        pattern = configs['pattern']
                        pattern_value = pattern['step']['1']['field_value']

                        players = tree.xpath(pattern_value)
                        # players = tree.find(pattern_value)
                        # players = tree.find('.//div')



                        embeded_player = configs['format_player']['step']['1']['field_value']
                        for x in players:
                            # array_player_id.append()
                            array_player_id.append(dict(x.attrib)[attribute_pattern_value])  # get value by attribute
                            array_player.append(str(etree.tostring(x, pretty_print=True)))

                            embeded = embeded_player.replace("{1}", dict(x.attrib)[attribute_pattern_value])
                            array_embeded_player.append(embeded)

                            x.append(etree.HTML(embeded))

                        content = etree.tostring(tree, method='html', pretty_print=True)

                        _val['content'] = str(content).replace('\\n', "").replace('\\t', "").replace("b'", "")



                except Exception as error:
                    pass
                if content_im != None and len(content_im) > 0:
                    directory1, directory2, directory3, directory4, directory5, directory6, imageName = \
                        content_im[i].images[0]['image_full_content'].split("/")
                    directory7, directory8, directory9, directory10, directory11, directory12, imageName1 = \
                        content_im[i].images[0]['image_filter_content'].split("/")
                    _val['image_full_content'] = directory6 + "-" + imageName
                    _val['image_filter_content'] = directory12 + "-" + imageName1
                # data_master.append({'key': k, 'value': json.loads(v)})
                data_master.append({'key': k, 'value': _val})
                i = i + 1
    except Exception as ex:
        flash('ERROR:' + ex.message, 'danger')
    pagination = Pagination(int(1), 1, len(data_master))
    return render_template('repository/pagedetail.html', sources=get_source(), data=data_master, link_href=cont.href,
                           pagination=pagination,
                           contentid=cid, source=s,
                           params={'source': source, 'tag': tag, 'published_from': published_from,
                                   'published_to': published_to, 'kw': kw,
                                   'pageid': PAGE_DETAIL, 'page': page, 'prepageid': PAGE_SEARCH})


@repository.route('/back_from_detail_to_filter_by_default/<page>', methods=['GET'])
def back_from_detail_to_filter_by_default(page):
    if not session.get('logged_in'):
        return render_template("login.html")
    aDict = get_data_from_service_filter_by_default(page)
    return render_template('repository/index2.html', sources=get_source(), contents=aDict['items'],
                           pagination=aDict['pagingnation'], params={'pageid': PAGE_FILTER_DEFAULT})


@repository.route('/back_from_detail_to_filter_by_timing/<sid>/<ptimingid>/<page>', methods=['GET'])
def back_from_detail_to_filter_by_timing(sid, ptimingid, page):
    if not session.get('logged_in'):
        return render_template("login.html")
    aDict = get_data_from_service_filter_by_timing(sid, ptimingid, page)
    return render_template('repository/index2.html', sources=get_source(), contents=aDict['items'],
                           pagination=aDict['pagingnation'],
                           params={'pageid': PAGE_FILTER_BY_TIMING, 'sid': sid, 'ptimingid': ptimingid})


@repository.route('/back_from_detail_to_search/<source>/<tag>/<published_from>/<published_to>/<kw>/<page>',
                  methods=['GET'])
def back_from_detail_to_search(source='', tag='', published_from='', published_to='', kw='', page=0):
    if not session.get('logged_in'):
        return render_template("login.html")
    content_service = ContentService()
    if published_from !='*':
        published_from = published_from.split('-')[::-1]
        published_from = '-'.join(published_from)

    if published_to != '*':
        published_to = published_to.split('-')[::-1]
        published_to = '-'.join(published_to)

    content = content_service.search(source, tag, published_from, published_to, kw, int(page), 50)
    count_items = content['response']['numFound']
    p = int(page)
    if p == 0:
        p = 1
    pagination = Pagination(p, 50, count_items)

    data_master = []
    for item in content['response']['docs']:
        data_master.append(item)
    return render_template('repository/index2.html', sources=get_source(), contents=data_master,
                           pagination=pagination,
                           params={'source': source, 'tag': tag, 'published_from': published_from,
                                   'published_to': published_to, 'kw': kw, 'page': page,
                                   'pageid': PAGE_SEARCH})


@repository.route('/report_source/', methods=['GET'])
def report_source():
    sources = get_source();
    tag_service = core.api.services.tag_service.TagService()
    for source in sources:
        source.tags = tag_service.get_by_source(str(source.id))
    return render_template('source_datatable.html', sources=sources, params={'pageid': PAGE_REPORT_SOURCE})


@repository.route('/report_tag/<sid>', methods=['GET'])
def report_tag(sid):
    tag_service = core.api.services.tag_service.TagService()
    tags = tag_service.get_by_source(str(sid))
    return render_template('tag_datatable.html', tags=tags, params={'pageid': PAGE_REPORT_TAG})

# @repository.route('/detail/<cid>', methods=['GET'])
# def detail(cid):
#     cont = content_impl.get_byid(cid)
#     configuration = configuration_impl.get_config('SOURCE', cont.source_id)
#     # n_dict = json.loads(cont.data)
#     data_master = []
#
#     try:
#         for item in cont.data:
#             for k, v in item.items():
#
#                 _val = json.loads(v)
#                 content = _val['content']
#                 try:
#                     if configuration['config']['PARSERVIDEOS']:
#                         configs = configuration['config']['PARSERVIDEOS']['data']
#                         array_player = []
#                         array_embeded_player = []
#                         array_player_id = []
#                         htmlparser = etree.HTMLParser(recover=True, remove_blank_text=True)
#                         # tree = etree.parse(StringIO(content), htmlparser)
#                         tree = etree.fromstring(str(content), htmlparser)
#
#                         attribute = configs['attribute']
#                         attribute_pattern_value = attribute['step']['1']['field_value']
#
#                         pattern = configs['pattern']
#                         pattern_value = pattern['step']['1']['field_value']
#
#                         players = tree.xpath(pattern_value)
#                         # players = tree.find(pattern_value)
#                         # players = tree.find('.//div')
#
#
#
#                         embeded_player = configs['format_player']['step']['1']['field_value']
#                         for x in players:
#                             # array_player_id.append()
#                             array_player_id.append(dict(x.attrib)[attribute_pattern_value])  # get value by attribute
#                             array_player.append(str(etree.tostring(x, pretty_print=True)))
#
#                             embeded = embeded_player.replace("{1}", dict(x.attrib)[attribute_pattern_value])
#                             array_embeded_player.append(embeded)
#
#                             x.append(etree.HTML(embeded))
#
#                         content = etree.tostring(tree, method='html', pretty_print=True)
#
#                         _val['content'] = str(content).replace('\\n', "").replace('\\t', "").replace("b'", "")
#
#
#
#                 except Exception as error:
#                     pass
#
#                 # data_master.append({'key': k, 'value': json.loads(v)})
#                 data_master.append({'key': k, 'value': _val})
#     except Exception as ex:
#         flash('ERROR:' + ex.message, 'danger')
#
#     return render_template('repository/detail.html', data=data_master, link_href=cont.href, contentid=cid)
