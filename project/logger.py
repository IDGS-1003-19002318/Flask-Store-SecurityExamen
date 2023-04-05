import logging

class Logger:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        self.file_handler = logging.FileHandler('{}.log'.format(self.name))
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
        
    def debug(self, message):
        self.logger.debug(message)
        
    def info(self, message):
        self.logger.info(message)
        
    def warning(self, message):
        self.logger.warning(message)
        
    def error(self, message):
        self.logger.error(message)
        
    def critical(self, message):
        self.logger.critical(message)
        
    def exception(self, message):
        self.logger.exception(message)
        
    def log(self, message):
        self.logger.info(message)
        

