# -*- coding: utf-8 -*-
import scrapy


class ScrapyKafkaItem(scrapy.Item):
    url = scrapy.Field()
