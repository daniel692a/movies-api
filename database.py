from peewee import *
import os
from dotenv import dotenv_values
from datetime import datetime

#load_dotenv(find_dotenv())
config = dotenv_values('.env')

database = MySQLDatabase('movies',
                            user=config['USER'],
                            password=config['PASSWORD'],
                            host=config['HOST'],
                            port=3306)


class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'

class Movie(Model):
    title = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title

    class Meta:
        database = database
        table_name = 'movies'

class UserReview(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref='reviews')
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.user.username} reviewed {self.movie.title}'

    class Meta:
        database = database
        table_name = 'user_reviews'
