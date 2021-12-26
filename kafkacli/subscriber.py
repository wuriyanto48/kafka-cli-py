import threading
from kafkacli.logger import logger as log

from abc import (
    ABC, 
    abstractmethod
)

from confluent_kafka import (
    Consumer,
)

from kafkacli.killer import (
    Killer,
)

from kafkacli.args_parser import (
    ArgsParser,
    CLIENT_ID,
    GROUP_ID,
)

'''
Subscriber a base class for kafka consumer
'''
class Subscriber(ABC):

    @abstractmethod
    def subscribe(self, topic):
        pass

    @abstractmethod
    def close():
        pass

class KSubscriber(Subscriber, threading.Thread):

    def __init__(self, arg_parser: ArgsParser, killer: Killer):
        threading.Thread.__init__(self, 
            name='kafka subscriber thread', daemon=True)
        self.killer = killer
        self.topic = arg_parser.topic
        
        config = {
            'bootstrap.servers': ','.join(arg_parser.brokers),
            'client.id': CLIENT_ID,
            'group.id': GROUP_ID,
            'auto.offset.reset': 'earliest'
        }

        if arg_parser.auth:
            config.update({
                'security.protocol': 'SASL_PLAINTEXT',
                'sasl.mechanism': 'PLAIN',
                'sasl.username': arg_parser.username,
                'sasl.password': arg_parser.password
            })

        self.kafka_subscriber = Consumer(config)
    
    def subscribe(self, topic):
        def on_assign(consumer, partitions):
            log.info('subscribed')

        try:
            self.kafka_subscriber.subscribe([topic], on_assign=on_assign)
            
            while True:
                message = self.kafka_subscriber.poll(timeout=1.0)
                if self.killer.killed:
                    break
                
                if message is None:
                    continue

                if message.error():
                    log.error('read message error')
                
                # commit message
                self.kafka_subscriber.commit(asynchronous=False)

                log.info('received message from topic {t}'.format(t=message.topic()))
                print(message.value().decode('utf-8'))
        except:
            log.error('error subscribing to brokers')
        
        self.close()

    def run(self):
        log.info('start kafka subscriber inside thread {tn}'.format(tn=self.name))
        self.subscribe(self.topic)
    
    def close(self):
        if self.kafka_subscriber is not None:
            self.kafka_subscriber.close()
