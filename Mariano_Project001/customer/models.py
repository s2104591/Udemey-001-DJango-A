from django.db import models

# Create your models here.


class CustomerModel(models.Model):
    firstname = models.CharField(max_length=200)
    username = models.CharField(max_length=100,unique=False)
  
    comments = models.CharField(max_length=200,default="not specified")
    password = models.CharField(max_length=100,default="-")
    passwordconfirm  = models.CharField(max_length=100,default="-")
    dob = models.DateField()
    


    def __str__(self):
        return f"Hello {self.firstname}"

    pass
