from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

# Create your models here.


class Customer(models.Model):
    user= models.ForeignKey( User,on_delete=models.SET_NULL,null=True,blank=True )
    preference1=models.CharField(max_length=200, default="not specified")
    userID=models.BigIntegerField(default=0)


    #reference
    #borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    pass


