import os



class RequestURL:
    def __init__(self):
        #---------------------------- PUBLISHING TIMMING---------------------------------------------
        self.PUBLISHTIMING_URL_LISTBYSOURCE = os.environ.get('PUBLISHTIMING_URL_LISTBYSOURCE')
        #--------------------------------------------------------------------------------------------

        #---------------------------- TAG -----------------------------------------------------------
        self.TAG_URL_LISTBYSOURCE = os.environ.get('TAG_URL_LISTBYSOURCE')
        #--------------------------------------------------------------------------------------------

        #---------------------------- CONTENT -------------------------------------------------------
        self.CONTENT_URL_FILTER_BY_TIMING = os.environ.get('CONTENT_URL_FILTER_BY_TIMING')
        #--------------------------------------------------------------------------------------------





