# kafka-cli-py

Kafka CLI tools written in <b>Python</b> for `publish` and `subscribe` message from <b>Apache Kafka</b>.

A similiar tool that i built with `Golang` https://github.com/musobarlab/kafka-cli.

### Install

Manual install
```shell
$ git clone https://github.com/wuriyanto48/kafka-cli-py.git
$ pip install -r requirements.txt
$ python setup.py install
```

### Usage
See available options
```shell
$ kafka-cli -h
```

#### Publish Message to Kafka
```shell
$ kafka-cli pub --brokers localhost:9092 --topic topbanget1 --message "hello world"
$ kafka-cli pub --brokers localhost:9092 --topic topbanget1 --message '{"header":"JSON","content":"this is JSON message"}'
```

#### Subscribe and get Message from Kafka
```shell
$ kafka-cli sub --brokers localhost:9092 --topic topbanget1
```

Multiple `brokers`
```shell
$ kafka-cli sub --brokers localhost:9092,localhost:9093,localhost:9094 --topic topbanget1
```

#### Show all topic
```shell
kafka-cli adm list-topic --brokers localhost:9092,localhost:9093,localhost:9094 --auth
```

#### Create new topic
```shell
$ kafka-cli adm create-topic --brokers localhost:9092,localhost:9093,localhost:9094 --topic topbanget1 --partition 3 --replication 3 --auth
```

#### Delete topic
```shell
$ kafka-cli adm delete-topic --brokers localhost:9092,localhost:9093,localhost:9094 --topic topic_name_to_delete --auth
```

#### Add partition to topic
```shell
$ kafka-cli adm add-partition --brokers localhost:9092,localhost:9093,localhost:9094 --topic existing_topic_name --partition 3 --auth
```

With `auth mechanism`, you need to provide `--auth` flag to prompt username and password
```shell
$ kafka-cli sub --brokers localhost:9092,localhost:9093,localhost:9094 --topic topbanget1 --auth
$ username: admin
$ password: adminpass
```