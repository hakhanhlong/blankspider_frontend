from ..request_helpers import RequestHelpers
from ..request_url import RequestURL
from dateutil.parser import parse
from dateutil.tz import *


class ContentService:

    def __init__(self):
        self.request_URL = RequestURL()
        self.requestHelpers = RequestHelpers()

    def filter_by_timing(self, source_id = '', publishtiming_id='', pageindex=0, pagesize=50):
        if pageindex == 0:
            pageindex = 1
        pageindex = (pageindex -1)*pagesize
        self.requestHelpers.url = self.request_URL.CONTENT_URL_FILTER_BY_TIMING % (publishtiming_id, source_id, pagesize, pageindex)
        #self.requestHelpers.params = {'source_id': source_id, 'publishtiming_id':publishtiming_id,
        #                              'pageindex':pageindex, 'pagesize':pagesize}

        return self.requestHelpers.get().json()

    def list_by_default(self, pageindex=1, pagesize=50):
        if pageindex == 0:
            pageindex = 1
        pageindex = (pageindex -1)*pagesize
        self.requestHelpers.url = self.request_URL.CONTENT_URL_LIST_BY_DEFAULT % (pagesize, pageindex)
        #self.requestHelpers.params = {'pageindex':pageindex, 'pagesize':pagesize}
        return self.requestHelpers.get().json()


    def search(self,source_id='', tagid='', published_from='', published_to='', keyword='', pageindex=1, pagesize=50):
        if pageindex == 0:
            pageindex = 1
        pageindex = (pageindex -1)*pagesize
        if published_from is not '*':
            published_from = parse(published_from)
            published_from = published_from.strftime('"%Y-%m-%dT00:00:00.000Z"')
        if published_to is not '*':
            published_to = parse(published_to)
            published_to = published_to.strftime('"%Y-%m-%dT00:00:00.000Z"')
        # if source_id == '*' and tagid == '*' and published_from == '*' and published_to == '*' and keyword is not '*':
        #     self.requestHelpers.url = 'http://118.107.88.35:8983/solr/lcbc_search/select?fl=title,published_at,tag_name,version_count,published_time,content_filter,id&indent=on&q='+keyword+'&rows='+str(pagesize)+'&start='+str(pageindex)+'&wt=json&fq=status:COMPLETED'
        # else:
        self.requestHelpers.url = self.request_URL.CONTENT_URL_SEARCH % (source_id, tagid, published_from, published_to, keyword, pagesize, pageindex)
        return self.requestHelpers.get().json()