"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 08/07/2019

"""
from .default import *


SECRET_KEY = SECRET_KEY_ENV

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'postgresql://'+ DB_USER + ':' + DB_PASS + '@' + DB_HOST + ':5432/' + DB_NAME
