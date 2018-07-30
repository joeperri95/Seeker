#Creates requests and handles responses

import requests
from bs4 import BeautifulSoup
from . import Result

class RequestManager:
	
	def __init__(self, urlList):
		self.urlList = urlList
		#list index to scan
		

	def scan(self):
		#create request, create and return the result objects
		
		res = list()
		sesh = requests.session()

		for index in range(len(self.urlList)):
			resp = sesh.get(self.urlList[index], data=None)

			soup =  BeautifulSoup((resp.text).encode('utf-8'), 'html.parser')

			#perhaps put class names into a file
			#otherwise use regex
			elem = soup.find_all('div', {'class' : [' row result','row result','  row result','lastRow row result','row sjlast result']})

			for i in range(0,len(elem)):
				description = self.processHTML(elem[i].find('span', {'class' : 'summary'}))
				company = self.processHTML(elem[i].find('span', {'class' : 'company'}))
				location = self.processHTML(elem[i].find('span', {'class' : 'location'}))
				title = self.processHTML(elem[i].a)
				link = self.processHTML(elem[i].a['href'])
				posting_id = self.processHTML(elem[i]['id'])

				res.append(Result(posting_id, title, company, description, link, location))

		resp.close()
		sesh.close()

		return res

	def processHTML(self, rawString):
		res = ""

		if(rawString):
			if(isinstance(rawString, str)):
				res = rawString.strip()
			else:
				res = rawString.text.strip()

			res.replace('"', ' ')

		return res

	def getFullText(self):
		sesh = requests.session()
		resp = sesh.get("")
		pass