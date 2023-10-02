"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 08/07/2019

"""
from .default import *
import os

SECRET_KEY = os.environ['SECRET_KEY_ENV']

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'postgresql://'+ os.environ['DB_USER'] + ':' + os.environ['DB_PASS'] + '@' + os.environ['DB_HOST'] + ':5432/' + os.environ['DB_NAME']
