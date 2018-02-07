# Scrapy-Kafka Demo

---
<h3 id="Start">开头说两句</h3>

* 使用中有什么问题的可以给我提issue，或者直接私聊我
* Email: 379978424@qq.com
* QQ: 379978424

---

<h3 id="Ready">准备工作</h3>

* Zookeeper环境（zookeeper-3.4.10） -> 具体安装下面讲 [安装步骤](#ZookeeperInstall)
* Kafka环境（kafka-1.0.0） -> 具体安装下面讲 [安装步骤](#KafkaInstall)
* 系统环境（Win10 x64）
* Python环境（Python 3.4.4）

---

<h3 id="Env">环境依赖</h3>

* 环境
    * Python3.4.4（Python2暂未测试,如果有测试过的给我提下issue）
* 依赖包
    * Scrapy
    * pykafka
* 安装方式:

```bash
windows: pip install requirements.txt
linux: pip3 install requiremnets.txt
```

---

<h3 id="Structure">项目结构</h3>

* consumer --- pykafka的消费者模块（测试接收以及之后接收爬虫数据）
* producer --- pykafka的生产者模块（测试发送）
* scrapy_kafka --- Scrapy + pykafka的爬虫（爬的是我学校的官网的所有a标签链接）

---

<h3 id="attention">需要注意的地方</h3>

* 爬虫部分我就不说了，我就挑特别的地方

1. kafka需要bytes数据,所以在pipeline接收到数据之后一定要encode;encode里面的encoding和消费者的decode编码要一致.
2. pipeline里面实现一个方法 close_spider(self, spider) 用来关闭producer;不然Scrapy会一直挂在producer那里不动. 
3. 我在pipeline里面判断了KAFKA_IP_PORT这个配置写的参数:
    * 单机部署可以用list或者str表示.
    * 伪分布或者全分布可以用list,或者用逗号隔开都可以.

---

<h3 id="ZookeeperInstall">Zookeeper安装</h3>

* 我大致说下Zookeeper的安装过程(以下都是单点测试, 伪分布和全分布还请各位完整学习完后再搭建)

1. 下载zookeeper.[下载地址](https://www.apache.org/dyn/closer.cgi/zookeeper/)
2. 解压在conf\下把zoo_sample.cfg 复制为zoo.cfg
3. 在系统环境变量中创建ZOOKEEPER_HOME值为zookeeper的Home目录
4. 在PATH中添加zookeeper的bin目录.
5. 在cmd中运行 zkServer

---

<h3 id="KafkaInstall">Kafka安装</h3>

* 也一样是单点

1. 下载kafka并解压.[下载地址](http://kafka.apache.org/downloads)
2. 进入解压后的文件夹, 在conf下修改server.properties文件中log.dirs指定log目录
3. 配置系统环境变量KAFKA_HOME
4. 在PATH中添加kafka bin/windows的目录（linux的不用理windows那个文件夹）
5. 启动kafka: kafka-server-start <kafka目录下config里面的server.properties的路径>

* 关于kafka的测试

1. 创建topic：

```bash
kafka-topics --create --topic newtest --partitions 1 --replication-factor 1 --zookeeper localhost:2181 
```
* 意思是：创建一个topic; 名字：newtest; 分区：1个; 副本数：1个; zookeeper的监听地址(由于是单点且若未修改zoo.cfg, 则zookeeper默认在2181端口上运行)

2. 创建producer:

```bash
kafka-console-producer --broker-list localhost:9092 --topic newtest  
```

* 此时窗口会到达等待输入的状态，先别关闭也不着急输入。启动consumer先。

3. 创建consumer

```bash
kafka-console-consumer  --zookeeper localhost:2181 --topic newtest
```

* 当consumer创建成功后，回到producer的窗口输入一些字符什么的，看看consumer有没有出现(注：中文有可能是乱码,但不影响测试)

4. 其他操作就请各位去参见kafka的官方文档或者系统学习后看看命令行的使用。