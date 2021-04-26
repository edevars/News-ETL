from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db.env_load import Environment

import logging
logging.basicConfig(level=logging.INFO)


class DataBase:
    _engine = None

    def __init__(self):
        raise RuntimeError('Call engine() instead')

    @classmethod
    def engine(cls):
        if cls._engine is None:
            logging.info('Creating new engine of DB')
            cls._engine = cls.__new__(cls)
            env = Environment()
            connection_string = f"postgresql+psycopg2://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_SERVER}:{env.DB_PORT}/{env.DB_NAME}"
            cls._engine = create_engine(connection_string)
            logging.info('Engine succesfully created')
        return cls._engine