import configparser
from datetime import timedelta

config = configparser.ConfigParser()
config.read('config/config.ini')


class Config:
    SECRET_KEY = config['settings'].get('SECRET_KEY', 'default_secret_key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(config['settings'].get('JWT_ACCESS_TOKEN_EXPIRES', '2')))
    SQLALCHEMY_DATABASE_URI = config['settings'].get('DATABASE', 'sqlite:///database.db')
