"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 08/07/2019

"""
from .default import *
import os

SECRET_KEY = print(os.environ['SECRET_KEY_ENV'])

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'postgresql://'+ print(os.environ['DB_USER']) + ':' + print(os.environ['DB_PASS']) + '@' + print(os.environ['DB_HOST']) + ':5432/' + print(os.environ['DB_NAME'])
