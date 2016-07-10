# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class TravelasiaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = Field()
    Introduction = Field()
    city = Field()
    Destination = Field()
    QuickFact = Field()

class SplitItem(Item):
	Type = Field()
	Num = Field()

class CityItem(Item):
	a = Field()
		
 	
 		