import os
import shutil
import json

class FileManager:
	
	def __init__(self, urlFile):
		self.urlFile = urlFile
		self.checkFiles()
		

	def checkFiles(self):
		#add a url validation section or separate method
		resUrl = False
		print(os.getcwd())
		for f in os.listdir(os.getcwd()):
			if(f == self.urlFile):
				resUrl = True

		if(not resUrl):
			fp = open(self.urlFile, 'w')
			fp.close()

	def validateUrl(self, urlString):
		res = True
		#do some crazy algorithm here

		return res

	def addUrl(self, newUrl):	
		if(validateUrl(newUrl)):
			with open(self.urlFile, 'a') as u:
				u.write(str(newUrl) + '\n')
		else:
			pass	

	def removeUrl(urlToRemove):
		pass

	def compileList(self):
		urlList = []
		with open(self.urlFile,'r') as u:
			for line in u.readlines():
				if(self.validateUrl(u)):
					urlList.append(line)
				else:
					pass
		return urlList