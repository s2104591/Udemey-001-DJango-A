from django.db import models




# Create your models here.

class Teacher(models.Model):
    firstname=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}  teaches {self.subject}"

    
