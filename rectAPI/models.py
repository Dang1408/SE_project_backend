from django.db import models
# Create your models here.
from django.contrib import admin
from django.db.models.fields.related import ForeignKey

# Create your models here.

class order(models.Model):
    id_order = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_order')
    nameofc= models.CharField(max_length=50)
    totalcost = models.FloatField()
    note = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.id_order

