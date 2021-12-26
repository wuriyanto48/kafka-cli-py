from kafkacli.logger import logger as log

from abc import (
    ABC, 
    abstractmethod
)

from confluent_kafka import (
    Producer,
)

from kafkacli.args_parser import (
    ArgsParser,
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

    def __init__(self, arg_parser: ArgsParser):
        config = {
            'bootstrap.servers': ','.join(arg_parser.brokers),
            'client.id': CLIENT_ID,
            'group.id': GROUP_ID,
        }

        if arg_parser.auth:
            config.update({
                'security.protocol': 'SASL_PLAINTEXT',
                'sasl.mechanism': 'PLAIN',
                'sasl.username': arg_parser.username,
                'sasl.password': arg_parser.password
            })

        self.kafka_producer = Producer(config)

    def publish(self, topic: str, message):
        if isinstance(message, str):
            message = bytes(message, encoding='utf-8')
        
        def on_delivery(err, msg):
            if err is not None:
                log.info('Failed to deliver message: %s: %s' % (str(msg), str(err)))
            else:
                log.info('Message produced: %s' % (str(msg)))

        try:
            self.kafka_producer.produce(topic, value=message, on_delivery=on_delivery)
            self.kafka_producer.flush(PUBLISHER_TIMEOUT)
        except:
            log.error('error publish message to brokers')

    def close(self):
        pass