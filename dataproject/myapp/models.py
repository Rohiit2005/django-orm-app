from django.db import models
from django.contrib import admin

# Create your models here.
class student (models.Model):
    referencenumber=models.CharField(primary_key=True,max_length=20,help_text="reference number")
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    place=models.CharField(max_length=80,default='Chennai')

class studentAdmin(admin.ModelAdmin):
    list_display=('referencenumber','name','age','email','place')    
