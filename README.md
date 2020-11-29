# kafka-cli-py

Kafka CLI tools written in <b>Python</b> for `publish` and `subscribe` message from <b>Apache Kafka</b>

### Install

Manual install
```shell
$ git clone 
$ pip install -r requirements.txt
$ python setup.py install
```

### Usage
See available options
```shell
$ kafka-cli -h
```

Publish Message to Kafka
```shell
$ kafka-cli pub --brokers localhost:9092 --topic topbanget1 --message "hello world"
$ kafka-cli pub --brokers localhost:9092 --topic topbanget1 --message '{"header":"JSON","content":"this is JSON message"}'
```

Subscribe and get Message from Kafka
```shell
$ kafka-cli sub --brokers localhost:9092 --topic topbanget1
```