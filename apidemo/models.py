from django.db import models
from ninja import Schema

# Defining Models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
    
# an ORM (Object-Relational Mapping) model used to define the structure of your database table.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    published_date = models.DateField()
    isbn = models.IntegerField()

    def __str__(self):
        return self.title
# the schema is used to define the structure of data for validation and serialization

# validate incoming request data
class BookSchema(Schema):
    title: str
    author: str
    published_date: str
    isbn: str




