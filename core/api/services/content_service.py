from ..request_helpers import RequestHelpers
from ..request_url import RequestURL


class ContentService:

    def __init__(self):
        self.request_URL = RequestURL()
        self.requestHelpers = RequestHelpers()

    def filter_by_timing(self, source_id = '', publishtiming_id='', pageindex=0, pagesize=50):
        self.requestHelpers.url = self.request_URL.CONTENT_URL_FILTER_BY_TIMING % (publishtiming_id, source_id, pagesize, pageindex)
        #self.requestHelpers.params = {'source_id': source_id, 'publishtiming_id':publishtiming_id,
        #                              'pageindex':pageindex, 'pagesize':pagesize}

        return self.requestHelpers.get().json()

    def list_by_default(self, pageindex=1, pagesize=50):
        self.requestHelpers.url = self.request_URL.CONTENT_URL_LIST_BY_DEFAULT % (pagesize, pageindex)
        #self.requestHelpers.params = {'pageindex':pageindex, 'pagesize':pagesize}
        return self.requestHelpers.get().json()