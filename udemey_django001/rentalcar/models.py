from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class RentalModel(models.Model):
    firstname=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    rating=models.IntegerField(validators=[ MinValueValidator(18), MaxValueValidator(75) ] )
    comments=models.CharField(max_length=50, default="no comments")

    def __str__(self):
        return f"id={self.id} firstname={self.firstname}, surname={self.surname}, rating={self.rating}, comment={self.comments}"





