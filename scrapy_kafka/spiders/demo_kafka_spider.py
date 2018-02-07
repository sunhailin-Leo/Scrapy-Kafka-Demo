# -*- coding: UTF-8 -*-
"""
Created on 2018年2月7日
@author: Leo
@file: demo_kafka_spider.py
"""

import scrapy
from scrapy_kafka.items import ScrapyKafkaItem


class Demo(scrapy.Spider):

    name = "KafkaScrapy"

    def __init__(self, **kwargs):
        # URL
        self._url = ["http://www.gzcc.cn"]

        super().__init__(**kwargs)

    def start_requests(self):
        yield scrapy.Request(url=self._url[0], method="GET")

    def parse(self, response):
        url_list = response.xpath('//a[contains(@href, "gzcc")]/@href').extract()
        # 初始化Item
        item = ScrapyKafkaItem()
        # 循环写入
        for url in url_list:
            item['url'] = url
            yield item
