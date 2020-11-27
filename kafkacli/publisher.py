from abc import (
    ABC, 
    abstractmethod
)

from kafka import (
    KafkaProducer
)

from kafkacli.args_parser import (
    CLIENT_ID,
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
        self.kafka_producer = KafkaProducer(
            client_id=CLIENT_ID,
            bootstrap_servers=brokers, 
            api_version=(0, 10),
            request_timeout_ms=3000,
        )

    def publish(self, topic: str, message):
        if isinstance(message, str):
            message = bytes(message, encoding='utf-8')

        self.kafka_producer.send(topic, value=message)
        self.kafka_producer.flush(PUBLISHER_TIMEOUT)
    
    def close(self):
        if self.kafka_producer is not None:
            self.kafka_producer.close()