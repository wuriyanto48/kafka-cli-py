from abc import ABC, abstractmethod

'''
Parser a base class for parsing functionality
'''
class Parser(ABC):

    @abstractmethod
    def parse(self):
        pass