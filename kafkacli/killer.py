import signal

from kafkacli.logger import logger as log

'''
Killer a class for gracefully shutdown operation
'''
class Killer:
    def __init__(self):
        self.killed = False
        signal.signal(signalnum=signal.SIGINT, handler=self.kill)
        signal.signal(signalnum=signal.SIGTERM, handler=self.kill)
    
    def kill(self, signum, frame):
        log.info('signum: {s} received'.format(s=signum))
        self.killed = True