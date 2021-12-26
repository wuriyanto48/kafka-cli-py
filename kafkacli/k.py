import sys

from kafkacli.admin import (
    Admin,
)

from kafkacli.publisher import (
    KPublisher,
)

from kafkacli.subscriber import (
    KSubscriber,
)

from kafkacli.args_parser import (
    ArgsParser, 
    ADMIN_COMMAND,
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
        if self.arg_parser.command == ADMIN_COMMAND:
            admin = Admin(self.arg_parser)
            admin.run()
        elif self.arg_parser.command == PUBLISH_COMMAND:
            topic = self.arg_parser.topic
            message = self.arg_parser.message
            publisher = KPublisher(self.arg_parser)

            # send message to kafka
            publisher.publish(topic=topic, message=message)

            # close connection
            publisher.close()
        elif self.arg_parser.command == SUBSCRIBE_COMMAND:

            subscriber = KSubscriber(self.arg_parser, killer=self.killer)
            subscriber.start()
            subscriber.join()
        else:
            return