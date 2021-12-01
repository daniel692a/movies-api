from peewee import *

database = MySQLDatabase('movies',
                            user='root',
                            password='',
                            host='localhost',
                            port=3306)
