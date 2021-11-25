import psycopg2

from constants import *


def getDatabaseConnection():
    try:
        return psycopg2.connect(database=DB_DATABASE,
                                user=DB_USER,
                                password=DB_PASSWORD,
                                host=DB_HOST,
                                port=DB_PORT)
    except Exception as e:
        print(e)
        return e
