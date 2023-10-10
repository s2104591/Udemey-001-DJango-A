from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField( default=20, validators=[ MinValueValidator(18), MaxValueValidator(75) ] )
    salary=models.FloatField()

    #validators=[ MinValueValidator(18), MaxValueValidator(75) ]
    def __str__(self):
        return f"id={self.id} name={self.name}, age={self.age}, salary={self.salary}"

    pass



