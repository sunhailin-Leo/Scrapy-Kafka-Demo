# -*- coding: utf-8 -*-

# Scrapy
from scrapy.conf import settings

# PyKafka
from pykafka import KafkaClient


class ScrapyKafkaPipeline(object):
    def __init__(self):
        # 判断下配置里面个给的是啥
        # 1. 如果长度等于1, list只有一个数据, 如果是字符肯定大于1
        # 2. 否则, 判断类型是否是list, 是的话用 逗号分隔
        # 3. 否则就是一个字符串
        kafka_ip_port = settings['KAFKA_IP_PORT']
        if len(kafka_ip_port) == 1:
            kafka_ip_port = kafka_ip_port[0]
        else:
            if isinstance(kafka_ip_port, list):
                kafka_ip_port = ",".join(kafka_ip_port)
            else:
                kafka_ip_port = kafka_ip_port

        # 初始化client
        self._client = KafkaClient(hosts=kafka_ip_port)

        # 初始化Producer 需要把topic name变成字节的形式
        self._producer = \
            self._client.topics[
                settings['KAFKA_TOPIC_NAME'].encode(encoding="UTF-8")
            ].get_producer()

    def process_item(self, item, spider):
        """
        写数据到Kafka
        :param item:
        :param spider:
        :return:
        """
        if spider.name == "KafkaScrapy":
            self._producer.produce(item['url'].encode(encoding="UTF-8"))
            return item

    def close_spider(self, spider):
        """
        结束之后关闭Kafka
        :return:
        """
        if spider.name == "KafkaScrapy":
            self._producer.stop()
