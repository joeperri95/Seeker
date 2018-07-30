from . import Result
import sqlite3
import os

class DataBaseManager():
	def __init__(self, dbPath):
		
		self._conn = sqlite3.connect(dbPath)
		self.cursor = self._conn.cursor()
		self.checkTable()
		self.max = self.getNumberOfPostings()

	def __del__(self):
		self._conn.close()

	def checkTable(self):
		self.cursor.execute(""" CREATE TABLE IF NOT EXISTS postings 
			(posting_id TEXT PRIMARY KEY,
			title TEXT NOT NULL,
			company TEXT NOT NULL,
			description TEXT,
			link TEXT,
			score REAL, 
			location TEXT, 
			sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL) """)

		self._conn.commit()


	def insertPostings(self, resList):
		self.checkTable()

		for res in resList:
			if(isinstance(res,Result)):
				fieldList = [res.posting_id, res.title, res.company, res.description, res.link, res.score, res.location]
				self.cursor.executemany("INSERT OR REPLACE INTO postings (posting_id, title, company, description, link, score, location) VALUES(?, ?, ?, ?, ?, ?, ?)", (fieldList,))
		self._conn.commit()

	def queryNPostings(self, number):
		
		lim = 0

		if(number > self.max):
			lim = max
		elif(number <= self.max):
			lim = number
		else:
			lim = 0

		try:
			self.cursor.execute("SELECT * FROM postings ORDER BY sqltime DESC LIMIT (?)", (lim,))
		except:
			return 
			
		res = list()

		for _ in range(lim):

			queryRes = self.cursor.fetchone()
			if(not (queryRes is None or queryRes[0] is None or queryRes[1] is None or queryRes[2] is None or queryRes[3] is None or queryRes[4] is None or queryRes[5] is None or queryRes[6] is None)):
				res.append(Result(queryRes[0], queryRes[1], queryRes[2], queryRes[3], queryRes[4], queryRes[5], queryRes[6]))	

		return res

	def queryAllPostings(self):

		self.cursor.execute("SELECT * FROM postings ORDER BY sqltime DESC")
		res = list()

		for _ in range(self.getNumberOfPostings()):

			queryRes = self.cursor.fetchone()
			if(not (queryRes is None or queryRes[0] is None or queryRes[1] is None or queryRes[2] is None or queryRes[3] is None or queryRes[4] is None or queryRes[5] is None or queryRes[6] is None)):
				res.append(Result(queryRes[0], queryRes[1], queryRes[2], queryRes[3], queryRes[4], queryRes[5], queryRes[6]))	

		return res

	def getNumberOfPostings(self):

		self.cursor.execute("SELECT COUNT(*) FROM postings")
		res = self.cursor.fetchone()
		return res[0]
