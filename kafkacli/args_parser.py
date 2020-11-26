import argparse

from abc import ABC, abstractmethod

__version__ = '1.0.0'

class Parser(ABC):

    @abstractmethod
    def parse(self):
        pass

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
        
        sub_parser = self.main_parser.add_subparsers()

        publish_parser = sub_parser.add_parser(name='pub', help='publish message to one or more brokers')
        subscribe_parser = sub_parser.add_parser(name='sub', help='subscribe to one or more brokers with specific topic')

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

        self.brokers: list = None
        self.topic: str = None
        self.message: str = None
        self.verbose: bool = False
    
    def parse(self):
        args = self.main_parser.parse_args()

        self.brokers = args.brokers.split(',')
        self.topic = args.topic.strip()
        self.message = args.message.strip()
        self.verbose = args.V