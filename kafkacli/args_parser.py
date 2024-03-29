import argparse
import sys

from kafkacli.parser import (
    Parser,
)

from kafkacli.logger import logger as log

'''
__version__
'''
__version__ = '1.0.0'

ADMIN_COMMAND = 'adm'
ADMIN_LIST_TOPIC_COMMAND = 'list-topic'
ADMIN_CREATE_TOPIC_COMMAND = 'create-topic'
ADMIN_DELETE_TOPIC_COMMAND = 'delete-topic'
ADMIN_ADD_PARTITION = 'add-partition'

PUBLISH_COMMAND = 'pub'
SUBSCRIBE_COMMAND = 'sub'
CLIENT_ID = 'kafka-cli-py'
GROUP_ID = 'kafka-cli-py-group'

'''
ArgsParser a class represent flag and argument
'''
class ArgsParser(Parser):
    def __init__(self):

        self.main_parser = argparse.ArgumentParser(prog='kafka-cli', 
            description='CLI tool that helps you publish and consume kafka message via terminal')
        
        '''
        version command
        '''
        self.main_parser.version = '{prog} version: {version}' .format(prog=self.main_parser.prog, version=__version__)
        self.main_parser.add_argument('--version', action='version')
        self.main_parser.add_argument('-v', action='version')
        
        sub_parser = self.main_parser.add_subparsers(dest='sub_command')

        '''
        admin_parser arguments
        '''
        self.admin_parser = sub_parser.add_parser(
            name=ADMIN_COMMAND,
            help='kafka-cli adm sub-command --brokers localhost:9092'
        )

        admin_sub_parser = self.admin_parser.add_subparsers(dest='admin_sub_command')

        admin_list_topic_parser = admin_sub_parser.add_parser(
            name=ADMIN_LIST_TOPIC_COMMAND,
            help='kafka-cli adm list-topic --brokers localhost:9092'
        )

        admin_create_topic_parser = admin_sub_parser.add_parser(
            name=ADMIN_CREATE_TOPIC_COMMAND,
            help='kafka-cli adm create-topic --brokers localhost:9092 --topic newtopic --partition 3 --replication 2'
        )

        admin_delete_topic_parser = admin_sub_parser.add_parser(
            name=ADMIN_DELETE_TOPIC_COMMAND,
            help='kafka-cli adm delete-topic --brokers localhost:9092 --topic topic_to_delete'
        )

        admin_add_partition_parser = admin_sub_parser.add_parser(
            name=ADMIN_ADD_PARTITION,
            help='kafka-cli adm add-partition --brokers localhost:9092 --topic existing_topic --partition 3'
        )
        
        admin_list_topic_parser.add_argument(
            '--brokers', 
            type=str, 
            default='localhost:9092', 
            help='list or single of kafka brokers, separate with ",". Ex: "localhost:9091,localhost:9092"', 
            required=True
        )

        '''
        auth command
        '''
        admin_list_topic_parser.add_argument(
            '--auth', 
            type=bool, 
            const=True,
            default=False,
            nargs='?',
            help='kafka-cli with auth mode'
        )

        # ------------------------------------------------------------------------------------------------

        admin_add_partition_parser.add_argument(
            '--brokers', 
            type=str, 
            default='localhost:9092', 
            help='list or single of kafka brokers, separate with ",". Ex: "localhost:9091,localhost:9092"', 
            required=True
        )

        admin_add_partition_parser.add_argument(
            '--topic', 
            type=str,
            help='topic name', 
            required=True
        )

        admin_add_partition_parser.add_argument(
            '--partition', 
            type=int,
            default=1,
            help='how many partition you need to add'
        )

        '''
        auth command
        '''
        admin_add_partition_parser.add_argument(
            '--auth', 
            type=bool, 
            const=True,
            default=False,
            nargs='?',
            help='kafka-cli with auth mode'
        )

        # ------------------------------------------------------------------------------------------------

        admin_delete_topic_parser.add_argument(
            '--brokers', 
            type=str, 
            default='localhost:9092', 
            help='list or single of kafka brokers, separate with ",". Ex: "localhost:9091,localhost:9092"', 
            required=True
        )

        admin_delete_topic_parser.add_argument(
            '--topic', 
            type=str,
            help='topic name', 
            required=True
        )

        '''
        auth command
        '''
        admin_delete_topic_parser.add_argument(
            '--auth', 
            type=bool, 
            const=True,
            default=False,
            nargs='?',
            help='kafka-cli with auth mode'
        )

        # ------------------------------------------------------------------------------------------------
        admin_create_topic_parser.add_argument(
            '--brokers', 
            type=str, 
            default='localhost:9092', 
            help='list or single of kafka brokers, separate with ",". Ex: "localhost:9091,localhost:9092"', 
            required=True
        )

        admin_create_topic_parser.add_argument(
            '--topic', 
            type=str,
            help='topic name', 
            required=True
        )

        admin_create_topic_parser.add_argument(
            '--partition', 
            type=int,
            default=1,
            help='how many partition you need'
        )

        admin_create_topic_parser.add_argument(
            '--replication', 
            type=int,
            default=1,
            help='how many replication factor you need',
        )

        '''
        auth command
        '''
        admin_create_topic_parser.add_argument(
            '--auth', 
            type=bool, 
            const=True,
            default=False,
            nargs='?',
            help='kafka-cli with auth mode'
        )

        # ------------------------------------------------------------------------------------------------
        publish_parser = sub_parser.add_parser(
            name=PUBLISH_COMMAND, 
            help='kafka-cli sub --brokers localhost:9092 --topic topbanget1'
        )

        subscribe_parser = sub_parser.add_parser(
            name=SUBSCRIBE_COMMAND, 
            help='kafka-cli pub --brokers localhost:9092 --topic topbanget1 --message "hello world"'
        )

        '''
        publish_parser arguments
        '''
        publish_parser.add_argument(
            '--brokers', 
            type=str, 
            default='localhost:9092', 
            help='list or single of kafka brokers, separate with ",". Ex: "localhost:9091,localhost:9092"', 
            required=True
        )

        publish_parser.add_argument(
            '--topic', 
            type=str,
            help='topic name', 
            required=True
        )

        publish_parser.add_argument(
            '--message', 
            type=str,
            help='message that will be publish', 
            required=True
        )

        '''
        verbose command
        '''
        publish_parser.add_argument(
            '-V', 
            type=bool, 
            const=True,
            default=False,
            nargs='?',
            help='kafka-cli with verbose mode'
        )

        '''
        auth command
        '''
        publish_parser.add_argument(
            '--auth', 
            type=bool, 
            const=True,
            default=False,
            nargs='?',
            help='kafka-cli with auth mode'
        )

        '''
        subscribe_parser arguments
        '''
        subscribe_parser.add_argument(
            '--brokers', 
            type=str, 
            default='localhost:9092', 
            help='list or single of kafka brokers, separate with ",". Ex: "localhost:9091,localhost:9092"', 
            required=True
        )

        subscribe_parser.add_argument(
            '--topic', 
            type=str,
            help='topic name', 
            required=True
        )

        '''
        verbose command
        '''
        subscribe_parser.add_argument(
            '-V', 
            type=bool, 
            const=True,
            default=False,
            nargs='?',
            help='kafka-cli with verbose mode'
        )

        '''
        auth command
        '''
        subscribe_parser.add_argument(
            '--auth', 
            type=bool, 
            const=True,
            default=False,
            nargs='?',
            help='kafka-cli with auth mode'
        )

        self.command: str = None
        self.brokers: list = None
        self.topic: str = None
        self.message: str = None
        self.verbose: bool = False
        self.partition: int = 1
        self.replication_factor: int = 1
        self.auth: bool = False
        self.username: str = None
        self.password: str = None
    
    '''
    parse will parse
    command line flag and arguments
    '''
    def parse(self):
        args = self.main_parser.parse_args()
        self.command = args.sub_command
        
        if args.sub_command == ADMIN_COMMAND:
            self.admin_sub_command = args.admin_sub_command
            if args.admin_sub_command == ADMIN_LIST_TOPIC_COMMAND:
                self.brokers = args.brokers.split(',')
                if args.auth:
                    auth_fields = ['username: ', 'password: ']
                    responses = []
                    for f in auth_fields:
                        try:
                            response = input(f)
                            if len(response) <= 0:
                                log.info('invalid input %s' % f)
                            else:
                                responses.append(response)
                        except ValueError as e:
                            log.info('invalid input')
                    if len(responses) > 0:
                        self.username = responses[0]
                        self.password = responses[1]
                        self.auth = True
            elif args.admin_sub_command == ADMIN_CREATE_TOPIC_COMMAND:
                self.brokers = args.brokers.split(',')
                self.topic = args.topic.strip()
                self.partition = args.partition
                self.replication_factor = args.replication
                if args.auth:
                    auth_fields = ['username: ', 'password: ']
                    responses = []
                    for f in auth_fields:
                        try:
                            response = input(f)
                            if len(response) <= 0:
                                log.info('invalid input %s' % f)
                            else:
                                responses.append(response)
                        except ValueError as e:
                            log.info('invalid input')
                    if len(responses) > 0:
                        self.username = responses[0]
                        self.password = responses[1]
                        self.auth = True
            elif args.admin_sub_command == ADMIN_ADD_PARTITION:
                self.brokers = args.brokers.split(',')
                self.topic = args.topic.strip()
                self.partition = args.partition
                if args.auth:
                    auth_fields = ['username: ', 'password: ']
                    responses = []
                    for f in auth_fields:
                        try:
                            response = input(f)
                            if len(response) <= 0:
                                log.info('invalid input %s' % f)
                            else:
                                responses.append(response)
                        except ValueError as e:
                            log.info('invalid input')
                    if len(responses) > 0:
                        self.username = responses[0]
                        self.password = responses[1]
                        self.auth = True
            elif args.admin_sub_command == ADMIN_DELETE_TOPIC_COMMAND:
                self.brokers = args.brokers.split(',')
                self.topic = args.topic.strip()
                if args.auth:
                    auth_fields = ['username: ', 'password: ']
                    responses = []
                    for f in auth_fields:
                        try:
                            response = input(f)
                            if len(response) <= 0:
                                log.info('invalid input %s' % f)
                            else:
                                responses.append(response)
                        except ValueError as e:
                            log.info('invalid input')
                    if len(responses) > 0:
                        self.username = responses[0]
                        self.password = responses[1]
                        self.auth = True
            else:
                self.admin_parser.print_help()
                sys.exit(1)
        elif args.sub_command == PUBLISH_COMMAND:
            self.message = args.message.strip()
            self.brokers = args.brokers.split(',')
            self.topic = args.topic.strip()
            self.verbose = args.V

            if args.auth:
                auth_fields = ['username: ', 'password: ']
                responses = []
                for f in auth_fields:
                    try:
                        response = input(f)
                        if len(response) <= 0:
                            log.info('invalid input %s' % f)
                        else:
                            responses.append(response)
                    except ValueError as e:
                        log.info('invalid input')
                if len(responses) > 0:
                    self.username = responses[0]
                    self.password = responses[1]
                    self.auth = True
        elif args.sub_command == SUBSCRIBE_COMMAND:
            self.brokers = args.brokers.split(',')
            self.topic = args.topic.strip()
            self.verbose = args.V

            if args.auth:
                auth_fields = ['username: ', 'password: ']
                responses = []
                for f in auth_fields:
                    try:
                        response = input(f)
                        if len(response) <= 0:
                            log.info('invalid input %s' % f)
                        else:
                            responses.append(response)
                    except ValueError as e:
                        log.info('invalid input')
                if len(responses) > 0:
                    self.username = responses[0]
                    self.password = responses[1]
                    self.auth = True
        else:
            self.main_parser.print_help()
            sys.exit(1)