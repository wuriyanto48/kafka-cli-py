from kafkacli.logger import logger as log

from abc import (
    ABC, 
    abstractmethod
)

from confluent_kafka import (
    Producer,
)

from kafkacli.args_parser import (
    CLIENT_ID,
    GROUP_ID,
)

PUBLISHER_TIMEOUT = 3

'''
Publisher a base class for kafka produer
'''
class Publisher(ABC):

    @abstractmethod
    def publish(self, topic, message):
        pass
    
    @abstractmethod
    def close():
        pass

class KPublisher(Publisher):

    def __init__(self, brokers: list):
        config = {
            'bootstrap.servers': ','.join(brokers),
            'client.id': CLIENT_ID,
            'group.id': GROUP_ID,
        }
        self.kafka_producer = Producer(config)

    def publish(self, topic: str, message):
        if isinstance(message, str):
            message = bytes(message, encoding='utf-8')

        def on_delivery(err, msg):
            if err is not None:
                log.info('Failed to deliver message: %s: %s' % (str(msg), str(err)))
            else:
                log.info('Message produced: %s' % (str(msg)))

        self.kafka_producer.produce(topic, value=message, on_delivery=on_delivery)
        self.kafka_producer.flush(PUBLISHER_TIMEOUT)
    
    def close(self):
        pass