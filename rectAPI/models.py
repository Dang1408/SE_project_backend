from django.db import models
# Create your models here.
from django.contrib import admin
from django.db.models.fields.related import ForeignKey

# Create your models here.

class order(models.Model):
    id_order = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_order')
    first_name= models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=15, default='0')
    totalcost = models.FloatField(default=0)
    note = models.CharField(max_length=100, default='')
    date = models.DateField(auto_now_add=True)


