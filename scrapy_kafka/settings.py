# -*- coding: utf-8 -*-

BOT_NAME = 'scrapy_kafka'

SPIDER_MODULES = ['scrapy_kafka.spiders']
NEWSPIDER_MODULE = 'scrapy_kafka.spiders'


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.1.3228.1 Safari/537.36'

ROBOTSTXT_OBEY = True

# kafka配置
# Kafka的访问ip或者端口（默认localhost:9092）
KAFKA_IP_PORT = ["localhost:9092"]
# Kafka的Topic name
KAFKA_TOPIC_NAME = "scrapy_kafka"

# 默认请求头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#    'scrapy_kafka.middlewares.ScrapyKafkaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy_kafka.middlewares.ScrapyKafkaDownloaderMiddleware': 543,
# }

# Configure item pipelines
ITEM_PIPELINES = {
   'scrapy_kafka.pipelines.ScrapyKafkaPipeline': 300,
}
