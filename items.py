# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class CarhomeItem(Item):
      collection = 'details'
      name = Field()
      level = Field()
      body_structure = Field()
      engine = Field()
      gearbox = Field()
      color = Field()
      guidance_price = Field()
      score = Field()
      detail_url = Field()
