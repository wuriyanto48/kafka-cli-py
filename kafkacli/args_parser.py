import argparse

from kafkacli.parser import (
    Parser,
)

'''
__version__
'''
__version__ = '1.0.0'

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

        self.command: str = None
        self.brokers: list = None
        self.topic: str = None
        self.message: str = None
        self.verbose: bool = False
    
    '''
    parse will parse
    command line flag and arguments
    '''
    def parse(self):
        args = self.main_parser.parse_args()
        self.command = args.sub_command
        
        if args.sub_command == PUBLISH_COMMAND:
            self.message = args.message.strip()
            self.brokers = args.brokers.split(',')
            self.topic = args.topic.strip()
            self.verbose = args.V
        elif args.sub_command == SUBSCRIBE_COMMAND:
            self.brokers = args.brokers.split(',')
            self.topic = args.topic.strip()
            self.verbose = args.V
        else:
            self.main_parser.print_help()