from ..request_helpers import RequestHelpers
from ..request_url import RequestURL

class TagService:

    def __init__(self):
        self.request_URL = RequestURL()
        self.requestHelpers = RequestHelpers()

    def get_by_source(self, source_id = '5d4b817b9d9a2507bc26ed36'):
        self.requestHelpers.url = self.request_URL.TAG_URL_LISTBYSOURCE
        self.requestHelpers.params = {'source_id': '5d4b817b9d9a2507bc26ed36'}

        try:

            list_data = self.requestHelpers.post_json().json()
            #list_data = self.requestHelpers.post_json()
        except Exception as e:
            error = e.message

        return list_data
