# -*- coding:utf-8 -*-
from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.title
	except AttributeError as e:
		return None
	return title

if __name__ == "__main__":
	title = getTitle("https://baidu.com")
	if title == None:
		print("Title Not found")
	else:
		print(title)
