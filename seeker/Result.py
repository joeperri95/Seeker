#result model

import time

class Result:
    def __init__(self,posting_id,title,company,description,link,location,score=0):
        self.posting_id = posting_id
        self.title = title
        self.company = company
        self.link = link
        self.description = description
        self.score = score
        self.location = location
        self.fulltext = ""
    
    def __repr__(self):
        return self.toJson()

    def toJson(self):
        outputJson = str('{ "posting_id" : '+ self.enc(self.posting_id) +', "company" : ' \
            + self.enc(self.company) +', "title" :'+ self.enc(self.title)  + ', "description" : ' \
            + self.enc(self.description) +', "location" : '+ self.enc(self.location) +', "link" : ' \
            + self.enc(self.link)+' , "score" : '+ self.enc(self.score)+'}')

        return outputJson

    def enc(self, s):
        return '"' + str(s) + '"'

    def scoring(self):
        pass
