from django.contrib import admin

# Register your models here.

from .models import Car


class CarAdmin(admin.ModelAdmin):
    # model, year, price
    fieldsets = [
        #('segnametname', { 'fields': ['fld1'] } ),
        ('car models', { 'fields': ['model'] } ),
        ('car year', { 'fields': ['year'] } ),
        ('car price', { 'fields': ['price'] } ),



    ]    

admin.site.register(Car, CarAdmin)

