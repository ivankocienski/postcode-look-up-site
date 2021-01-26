import os

_DEFAULT_NAME = 'postcode_server'
_DEFAULT_ENV = 'development'
_DEFAULT_HOST = '127.0.0.1'
_DEFAULT_PORT = 5000
_DEFAULT_DB_URL = 'sqlite:///db/database.sqlite'

work_dir = os.getcwd()

def name():
    return os.getenv('APP_NAME', _DEFAULT_NAME)

def env():
    return os.getenv('APP_ENV', _DEFAULT_ENV)

def host():
    return os.getenv('APP_HOST', _DEFAULT_HOST)

def port():
    return os.getenv('APP_PORT', _DEFAULT_PORT)

def db_url():
    return os.getenv('APP_DB_URL', _DEFAULT_DB_URL)
