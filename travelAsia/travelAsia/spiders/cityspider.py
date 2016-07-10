# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from travelAsia.items import TravelasiaItem
from travelAsia.items import SplitItem
import re
from bs4 import BeautifulSoup
from urllib2 import urlopen


class City(scrapy.Spider):
	name = "cityAsia"
	#redis_key = 'cityAsia:'
	start_urls = ['http://wikitravel.org/en/Nepal']

	url = 'http://wikitravel.org/en/'

	def parse(self,response):
		item = TravelasiaItem()

		selector = Selector(response)
		Infos = selector.xpath('//div[@id="mw-content-text"]/table')
		QuickFact = selector.xpath('//div[@id="quickbar"]/table')
		QuickFacts = BeautifulSoup(str(QuickFact.extract())).findAll("tr")
		Cities = Infos.xpath('//td[@valign="top"]/ul[13]/li')
		otherDes = Infos.xpath('//td[@valign="top"]/ul[14]/li')
		Introduction = BeautifulSoup(str(Infos.xpath('//td[@valign="top"]/p[1]').extract())).get_text()
		
		#CitiesInfos = Infos.xpath('//td[@valign="top"]/ul[13]/li/a/text()').extract()

		cityList = []
		DesList = []
		QuickList = {}
		for eachcity in Cities:
		
			bsCity = BeautifulSoup(eachcity.extract())
			Cityname = bsCity.a.get_text()
			bsCity.findAll("a")
			cityDict = {"Cityname":Cityname,"cityInfo":bsCity.li.get_text(),"wikiUrl":self.url + Cityname}
			cityList.append(cityDict)

		for eachDes in otherDes:
			bsDes = BeautifulSoup(eachDes.extract())
			Desname = bsDes.a.get_text()
			DesDict = {"Desname":Desname,"DesInfo":bsDes.li.get_text(),"wikiUrl":self.url+Cityname}
			DesList.append(DesDict)

		for each in QuickFacts:
			tmp = each.findAll("td")
			if len(tmp)>1 and tmp[0].b and tmp[1] :
				QuickList[tmp[0].b.get_text()] = tmp[1].get_text()
		
		
		flag = SplitItem()
		flag["Type"] = "Country"
		flag["Num"] = 1
		yield flag

		item["country"] = "Nepal"
		item["Introduction"] = Introduction
		item["city"] = cityList
		item["Destination"] = DesList
		item["QuickFact"] = QuickList
		yield item	

		for eachone in Cities:
			print eachone["wikiUrl"]
		html = urlopen("http://www.baidu.com/")
		bsB = BeautifulSoup(html).title
		print bsB
		
		#Destinations = Infos.xpath('//td[@valign="top"]/ul[14]').extract()
		
		
		