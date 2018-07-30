from flask import Flask, render_template, request, redirect, url_for, flash
import sys
import os
'''
from seeker import DataBaseManager
from seeker import RequestManager
from seeker import FileManager
from seeker import Result
'''
from FlaskApp.seeker import DataBaseManager
from FlaskApp.seeker import RequestManager
from FlaskApp.seeker import FileManager
from FlaskApp.seeker import Result

ABS_PATH = '/var/www/FlaskApp/FlaskApp/'
os.chdir(ABS_PATH)
app = Flask(__name__)
app.secret_key = 'ayy lmao'

dbm = DataBaseManager('results.db')
#fm = FileManager('urls.txt')
#req = RequestManager(fm.compileList())
postings = dbm.queryNPostings(dbm.getNumberOfPostings())

class dataHandler():
	def __init__(self):
		self.ptr = 5
		self.next = 10
		self.max = dbm.getNumberOfPostings()

b = dataHandler()

@app.route('/')
def homepage():
	#return render_template('base.html')
	
	b.ptr = 0
	b.next = 5
	return redirect(url_for('forward', res=5))
	
@app.route('/results/<int:res>', methods=['GET', 'POST'])
def forward(res):
	b.ptr = (b.ptr + 5) if (b.ptr + 5 < b.max) else b.max
	b.next = (b.next + 5) if (b.next + 5 < b.max) else b.max
	return render_template("main.html", files = postings, b = b)

@app.route('/scan', methods=['GET', 'POST'])
def scan():
	
	dbm = DataBaseManager('results.db')
	fm = FileManager('urls.txt')
	req = RequestManager(fm.compileList())
	

	l = req.scan()
	num = len(l)

	dbm.insertPostings(l)
	postings = dbm.queryNPostings(dbm.getNumberOfPostings())

	b.ptr = 0
	b.next = 5
	flash(num)
	return redirect(url_for('forward', res=5))

if __name__ == "__main__":
	app.run()
