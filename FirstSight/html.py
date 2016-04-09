# get html!

from urllib2 import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://baidu.com/")
bsObj =  BeautifulSoup(html.read())
print (bsObj.title)
