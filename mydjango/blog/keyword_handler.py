import alchemyapi

class KeywordHandler(object):

    def __init__(self):
        self.keyword_extracter = alchemyapi.AlchemyAPI()

    def get_kw_for_url(self, url):
        alchemy_res = self.keyword_extracter.keywords("url", url)
        res = []
        for item in alchemy_res['keywords']:
            kws = item['text']
            kws_list = kws.split(" ")
            res = res + kws_list
        return res
