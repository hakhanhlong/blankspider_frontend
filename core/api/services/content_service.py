from ..request_helpers import RequestHelpers
from ..request_url import RequestURL


class ContentService:

    def __init__(self):
        self.request_URL = RequestURL()
        self.requestHelpers = RequestHelpers()

    def filter_by_timing(self, source_id = '', publishtiming_id='', pageindex=1, pagesize=20):
        self.requestHelpers.url = self.request_URL.CONTENT_URL_FILTER_BY_TIMING
        self.requestHelpers.params = {'source_id': source_id, 'publishtiming_id':publishtiming_id,
                                      'pageindex':pageindex, 'pagesize':pagesize}

        return self.requestHelpers.post_json().json()