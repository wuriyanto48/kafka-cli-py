import sys
from kafkacli.publisher import (
    KPublisher,
)

from kafkacli.subscriber import (
    KSubscriber,
)

from kafkacli.args_parser import (
    ArgsParser, 
    PUBLISH_COMMAND,
    SUBSCRIBE_COMMAND,
)

from kafkacli.killer import (
    Killer,
)

class K:
    def __init__(self, arg_parser: ArgsParser, killer: Killer):
        self.arg_parser = arg_parser
        self.killer = killer
    
    def run(self):
        if self.arg_parser.command == PUBLISH_COMMAND:
            brokers = self.arg_parser.brokers
            topic = self.arg_parser.topic
            message = self.arg_parser.message
            publisher = KPublisher(brokers)

            # send message to kafka
            publisher.publish(topic=topic, message=message)

            # close connection
            publisher.close()
        elif self.arg_parser.command == SUBSCRIBE_COMMAND:
            brokers = self.arg_parser.brokers
            topic = self.arg_parser.topic

            subscriber = KSubscriber(brokers, killer=self.killer, topic=topic)
            subscriber.start()
            subscriber.join()
        else:
            return