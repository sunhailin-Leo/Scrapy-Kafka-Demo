# -*- coding: UTF-8 -*-
"""
Created on 2018年2月7日
@author: Leo
@file: kafka_consumer.py
"""

# Zookeeper启动命令: zkServer
# Kafka启动命令: kafka-server-start F:\Kafka_zookeeper\kafka_2.12-1.0.0\config\server.properties


from pykafka import KafkaClient
from pykafka.common import OffsetType

client = KafkaClient(hosts="localhost:9092")
# 要用字节形式
topic = client.topics[b'scrapy_kafka']
# 用的是get_simple_consumer做测试
consumer = topic.get_simple_consumer(
    consumer_group=b"scrapy_kafka",
    auto_offset_reset=OffsetType.EARLIEST,
    reset_offset_on_start=True
)
for x in consumer:
    if x is not None:
        print(x.value.decode('utf-8'))

