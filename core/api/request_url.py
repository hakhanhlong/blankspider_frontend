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
        #self.CONTENT_URL_FILTER_BY_TIMING = 'http://118.107.88.25:8096/api/v1/content/filter_by_timing'
        self.CONTENT_URL_FILTER_BY_TIMING = 'http://118.107.88.35:8983/solr/lcbc_search/select?fl=title,published_at,tag_name,version_count,published_time,id,source_id&fq=publishtiming_id:%s&fq=source_id:%s&indent=on&q=*&rows=%s&sort=published_at desc&start=%s&wt=json'

        #self.CONTENT_URL_LIST_BY_DEFAULT = 'http://118.107.88.25:8096/api/v1/content/listbydefault'

        self.CONTENT_URL_LIST_BY_DEFAULT = 'http://118.107.88.35:8983/solr/lcbc_search/select?fl=title,published_at,tag_name,version_count,published_time,id,source_id&indent=on&q=*:*&rows=%s&sort=published_at desc&start=%s&wt=json'

        #--------------------------------------------------------------------------------------------

        #--------------------------------------------------------------------------------------------


        self.CONTENT_URL_SEARCH = 'http://118.107.88.35:8983/solr/lcbc_search/select?fl=title,published_at,tag_name,version_count,published_time,id, source_id&fq=source_id:%s&fq=tag_id:%s&fq=published_at:%s&indent=on&q=%s&rows=%s&sort=published_at desc&start=%s&wt=json'

        #--------------------------------------------------------------------------------------------

        self.CONTENT_URL_SEARCH_BY_KEYWORD = 'http://118.107.88.35:8983/solr/lcbc_search/select?fl=title,published_at,tag_name,version_count,published_time,id&indent=on&q=%s&wt=json';





