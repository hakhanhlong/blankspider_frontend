from ..request_helpers import RequestHelpers
from ..request_url import RequestURL

class TagService:

    def __init__(self):
        self.request_URL = RequestURL()
        self.requestHelpers = RequestHelpers()

    def get_by_source(self, source_id = ''):
        self.requestHelpers.url = self.request_URL.TAG_URL_LISTBYSOURCE
        self.requestHelpers.params = {'source_id': source_id}

        return self.requestHelpers.post_json().json()
