import threading
from kafkacli.logger import logger as log

from abc import (
    ABC, 
    abstractmethod
)

from kafka import (
    KafkaConsumer
)

from kafkacli.killer import (
    Killer,
)

from kafkacli.args_parser import (
    CLIENT_ID,
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

    def __init__(self, brokers: list, killer: Killer, topic: str = None):
        threading.Thread.__init__(self, 
            name='kafka subscriber thread', daemon=True)
        self.killer = killer
        self.topic = topic
        self.kafka_subscriber = KafkaConsumer(
            client_id=CLIENT_ID,
            auto_offset_reset='earliest',
            bootstrap_servers=brokers, 
            api_version=(0, 10),
        )
    
    def subscribe(self, topic):
        self.kafka_subscriber.subscribe([topic])
        while not self.killer.killed:
            for message in self.kafka_subscriber:
                log.info('received message from topic {t}: {m}'.format(t=message.topic, m=message.value))
        
        self.close()

    def run(self):
        log.info('start kafka subscriber inside thread {tn}'.format(tn=self.name))
        self.subscribe(self.topic)
    
    def close():
        if self.kafka_subscriber is not None:
            self.kafka_subscriber.close()
