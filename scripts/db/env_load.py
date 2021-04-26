# Handling environment
from dotenv import load_dotenv
import os
import logging
logging.basicConfig(level=logging.INFO)


class Environment:
    def __init__(self):
        load_dotenv()
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_SERVER = os.getenv('DB_SERVER')
        self.DB_PORT = os.getenv('DB_PORT')
        logging.info("Creating environment variables")
