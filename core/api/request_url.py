import os



class RequestURL:
    def __init__(self):
        #---------------------------- PUBLISHING TIMMING---------------------------------------------
        #self.PUBLISHTIMING_URL_LISTBYSOURCE = os.environ.get('PUBLISHTIMING_URL_LISTBYSOURCE')
        self.PUBLISHTIMING_URL_LISTBYSOURCE = 'http://118.107.88.25:8096/api/v1/publishtiming/list_by_source'
        #--------------------------------------------------------------------------------------------

        #---------------------------- TAG -----------------------------------------------------------
        #self.TAG_URL_LISTBYSOURCE = os.environ.get('TAG_URL_LISTBYSOURCE')
        self.TAG_URL_LISTBYSOURCE = 'http://118.107.88.25:8096/api/v1/tag/get_tag_bysource'
        #--------------------------------------------------------------------------------------------

        #---------------------------- CONTENT -------------------------------------------------------
        #self.CONTENT_URL_FILTER_BY_TIMING = os.environ.get('CONTENT_URL_FILTER_BY_TIMING')
        self.CONTENT_URL_FILTER_BY_TIMING = 'http://118.107.88.25:8096/api/v1/content/filter_by_timing'
        #--------------------------------------------------------------------------------------------





