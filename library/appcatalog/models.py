from django.db import models

# Create your models here.

class Genre(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self) :
        return self.name

    pass

class Book(models.Model):
    title= models.CharField(max_length=100)
    pass

class Author(models.Model):
    pass

class BookInstance(models.Model):
    pass

class B(models.Model):
    pass


