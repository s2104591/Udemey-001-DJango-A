from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Car(models.Model):
    model       =   models.CharField(max_length=50)   
    year        =   models.IntegerField(default=1900, validators=[ MinValueValidator(1900), MaxValueValidator(2100) ] )
    price       =   models.FloatField(default=0)
   



    def __str__(self):
        return f"id={self.id} model={self.model}, year={self.year}, price={self.price}"





