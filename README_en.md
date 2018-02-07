# Scrapy-Kafka Demo

---

* 中文介绍（Chinese）
Chinese README.md [Here](https://github.com/sunhailin-Leo/Scrapy-Kafka-Demo/blob/master/README.md)


---
<h3 id="Start">Say somethine</h3>

* If you meet some problem when running this demo, you can send email or make an issue to me.
* Email: 379978424@qq.com
* QQ: 379978424

---

<h3 id="Ready">Preparation</h3>

* Zookeeper Environment（zookeeper-3.4.10） ->  [Install Step](#ZookeeperInstall)
* Kafka Environment（kafka-1.0.0） ->  [Install](#KafkaInstall)
* System Environment（Win10 x64）
* Python Environment（Python 3.4.4）

---

<h3 id="Env">Dependency</h3>

* Environment
    * Python3.4.4（Python2 not test. If someone has tested it, please tell me or make an issue.）
* Library
    * Scrapy
    * pykafka
* How to install:

```bash
windows: pip install requirements.txt
linux: pip3 install requiremnets.txt
```

---

<h3 id="Structure">Project Structure</h3>

* consumer --- pykafka consumer module（Test reception and receive Scrapy data）
* producer --- pykafka producer modele（Test send something）
* scrapy_kafka --- Scrapy + pykafka spider（Crawl all html a tag from my campus website(main page).）

---

<h3 id="attention">Pay attention</h3>

* I choose some special point about kafka instead of Scrapy.

1. kafka need bytes data for transfer, so when pipeline are receive the data. You must use encode method; Encode method`s argument encoding should same as with consumer decode arguments.
2. Implement close_spider(self, spider) method in pipeline for shutdown the producer; Otherwise Scrapy will hang on for wating producer close. 
3. I code a method in pipeline to judge setting `KAFKA_IP_PORT`:
    * Single deployment can use list or str.
    * Pseudo distributed or fully distributed can use list, or use str(multiple IP and ports are separated by comma). -> e.g: "192.168.1.101:9092,192.168.1.102:9092"

---

<h3 id="ZookeeperInstall">Zookeeper Install</h3>

* Single Deployment

1. Download zookeeper.[Download link](https://www.apache.org/dyn/closer.cgi/zookeeper/)
2. Unzip the package, and get into `conf`, copy `zoo_sample.cfg` to `zoo.cfg` or rename.
3. set zookeeper `root path` as `ZOOKEEPER_HOME` as system environment variable
4. add zookeeper `bin` path in PATH.
5. run `zkServer` in cmd.

---

<h3 id="KafkaInstall">Kafka安装</h3>

* Single Deployment

1. Download kafka and unzip.[Download link](http://kafka.apache.org/downloads)
2. Get into `conf`, and edit `server.properties` variable `log.dirs` to somewhere you make folder for save log.
3. Configure system environment variable `KAFKA_HOME`.
4. add kafka bin/windows path in `PATH`（if you use linux juet set `bin` in `PATH`）
5. run kafka: kafka-server-start <the path absolute path of server.properties>

* Test kafka

1. Create topic：

```bash
kafka-topics --create --topic newtest --partitions 1 --replication-factor 1 --zookeeper localhost:2181 
```

2. Create producer:

```bash
kafka-console-producer --broker-list localhost:9092 --topic newtest  
```

* At the moment, the window is in the state of waiting for input. Don`t close it, please run consumer.

3. Create consumer

```bash
kafka-console-consumer  --zookeeper localhost:2181 --topic newtest
```

* When consumer is start success. You can back to producer window and input something. Then you can check consumer window receiver something you input at producer window.

4. Other kafka operation, please check the official document. 