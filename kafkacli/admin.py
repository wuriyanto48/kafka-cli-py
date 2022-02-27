from confluent_kafka.admin import (
    AdminClient,
    NewTopic,
    NewPartitions,
)

from kafkacli.args_parser import (
    ArgsParser,
    CLIENT_ID,
    ADMIN_LIST_TOPIC_COMMAND,
    ADMIN_CREATE_TOPIC_COMMAND,
    ADMIN_DELETE_TOPIC_COMMAND,
    ADMIN_ADD_PARTITION,
)

class Admin:
    def __init__(self, args: ArgsParser):
        self.args = args
        config = {
            'bootstrap.servers': ','.join(args.brokers),
            'client.id': CLIENT_ID,
        }

        if args.auth:
            config.update({
                'security.protocol': 'SASL_PLAINTEXT',
                'sasl.mechanism': 'PLAIN',
                'sasl.username': args.username,
                'sasl.password': args.password
            })
        
        print(config)

        self.admin_client = AdminClient(conf=config)
    
    def _get_topics(self):
        metadata = self.admin_client.list_topics(timeout=10)
        topics: dict = metadata.topics

        print()
        print('---Brokers List---')
        brokers: dict = metadata.brokers
        for key, val in brokers.items():
            print(key, val)
            # print('broker name : {bn}'.format(bn=key))

        print()
        print('---Topic List---')
        for key, val in topics.items():
            # print(val.partitions)
            print('topic name : {tn}'.format(tn=key))
    
    def _create_topic(self):
        topic = self.args.topic
        partition = self.args.partition
        replication = self.args.replication_factor

        new_topic = NewTopic(topic, num_partitions=partition, replication_factor=replication)
        res = self.admin_client.create_topics([new_topic])
        print('---New Created Topics---')
        for key, val in res.items():
            print('topic name : {tn}'.format(tn=key))
    
    def _create_partition(self):
        topic = self.args.topic
        partition = self.args.partition

        new_partition = NewPartitions(topic, partition)
        res = self.admin_client.create_partitions([new_partition])
        
        for key, val in res.items():
            try:
                val.result()  # The result itself is None
                print("new additional partitions created for topic {}".format(key))
            except Exception as e:
                print("faailed to add new additional partitions to topic {}: {}".format(key, e))

    def _delete_topic(self):
        pass
    
    def run(self):
        if self.args.admin_sub_command == ADMIN_LIST_TOPIC_COMMAND:
            self._get_topics()
        elif self.args.admin_sub_command == ADMIN_CREATE_TOPIC_COMMAND:
            self._create_topic()
        elif self.args.admin_sub_command == ADMIN_ADD_PARTITION:
            self._create_partition()
        else:
            return