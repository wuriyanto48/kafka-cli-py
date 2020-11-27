import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

console_formatter = logging.Formatter(FORMAT)
console_handler.setFormatter(console_formatter)

logger.addHandler(console_handler)