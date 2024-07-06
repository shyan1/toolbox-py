import logging

# Create a logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# Create a file handler
fh = logging.FileHandler('mylog.log')
fh.setLevel(logging.DEBUG)

# Create a console handler
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# Log some messages
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')
