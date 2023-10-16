from django.db import models
from django.contrib import admin





# Create your models here.
# note I explictly registered Teacher to the admin , unlike prevuiously


class Teacher(models.Model):
    firstname=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.surname}  teaches {self.subject}"

class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)        

    
