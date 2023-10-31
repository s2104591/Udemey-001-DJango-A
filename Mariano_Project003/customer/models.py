from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

# Create your models here.


class Customer(models.Model):
    # replaced by UserID
    user= models.ForeignKey( User,on_delete=models.SET_NULL,null=True,blank=True )
    
    preference1=models.CharField(max_length=200, default="not specified")
    userID=models.BigIntegerField(default=0)
    userName=models.CharField(max_length=100, default="?")
    email=models.CharField(max_length=200, default="?")
    firstname=models.CharField(max_length=100, default="?")
    lastname=models.CharField(max_length=100, default="?")



    #reference
    #borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        #return f"userID={self.userID}  username={self.userName}  preference1= {self.preference1}"
        return f"ID={self.id} userID={self.userID} {self.userName} {self.firstname} {self.lastname} {self.email}  preference1= {self.preference1}"

    pass


