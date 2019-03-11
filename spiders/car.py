# -*- coding: utf-8 -*-
import requests
from scrapy import Spider, FormRequest
from carhome.items import CarhomeItem
from bs4 import BeautifulSoup
import urllib.request



class CarSpider(Spider):
    name = 'car'
    allowed_domains = ['car.autohome.com.cn/']
    start_urls = ['https://car.autohome.com.cn/']

    def start_requests(self):
        base_url = 'https://car.autohome.com.cn/price/list-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-'
        max_page = self.settings.get('MAX_PAGE')
        for page in range(1, max_page + 1):
            print(page)
            url = base_url + str(page) + '.html'
            print(url)
            yield FormRequest(url, callback=self.parse_index, meta={'page': page}, dont_filter=True)
        # url = 'https://car.autohome.com.cn/price/list-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-1.html'
        # yield FormRequest(url, callback=self.parse_index)

    def parse_index(self, response):
        head = 'https://car.autohome.com.cn'
        details = response.xpath('//div[contains(@class, "list-cont-bg")]')
        for detail in details:
            item = CarhomeItem()
            item['name'] = detail.xpath('.//div[@class="main-title"]/a//text()').extract_first()
            item['level'] = detail.xpath('.//ul[@class="lever-ul"]/li[1]/span[@class="info-gray"]//text()').extract_first()
            item['body_structure'] = detail.xpath('.//ul[@class="lever-ul"]/li[2]/a//text()').extract_first()

            engine_list = detail.xpath('.//ul[@class="lever-ul"]/li[3]/span/a//text()').extract()
            temp = ""
            for text in engine_list: temp = temp + ' ' + text
            item['engine'] = temp

            gearbox_list = detail.xpath('.//ul[@class="lever-ul"]/li[4]/a//text()').extract()
            temp = ""
            for text in gearbox_list: temp = temp + ' ' + text
            item['gearbox'] = temp

            color_list = detail.xpath('.//ul[@class="lever-ul"]/li[5]/div[@class="carcolor fn-left"]/a/div[@class="tip"]/div//text()').extract()
            temp = ""
            for text in color_list: temp = temp + ' ' + text
            item['color'] = temp

            item['guidance_price'] = detail.xpath('.//span[@class="lever-price red"]/span//text()').extract_first()
            item['score'] = detail.xpath('.//span[@class="score-number"]//text()').extract_first()
            item['detail_url'] = head + detail.xpath('.//div[@class="list-cont-img"]/a/@href').extract_first()
            yield item
        print(item.collection)



