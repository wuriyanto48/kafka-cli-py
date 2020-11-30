from confluent_kafka.admin import (
    AdminClient,
    NewTopic,
)

from kafkacli.args_parser import (
    ArgsParser,
    CLIENT_ID,
    ADMIN_LIST_TOPIC_COMMAND,
    ADMIN_CREATE_TOPIC_COMMAND,
    ADMIN_DELETE_TOPIC_COMMAND,
)

class Admin:
    def __init__(self, args: ArgsParser):
        self.args = args
        config = {
            'bootstrap.servers': ','.join(args.brokers),
            'client.id': CLIENT_ID,
        }

        self.admin_client = AdminClient(conf=config)
    
    def _get_topics(self):
        metadata = self.admin_client.list_topics()
        topics: dict = metadata.topics

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

    def _delete_topic(self):
        pass
    
    def run(self):
        if self.args.admin_sub_command == ADMIN_LIST_TOPIC_COMMAND:
            self._get_topics()
        elif self.args.admin_sub_command == ADMIN_CREATE_TOPIC_COMMAND:
            self._create_topic()
        else:
            return