from django.db import models
import datetime
# Create your models here.
class S_IF(models.Model):
    C_NAME=models.CharField(max_length=200)
    NAME = models.CharField(max_length=200)
    INDUSTRY = models.CharField(max_length=200)
    EVENT = models.CharField(max_length=200)
    ADDRESS = models.CharField(max_length=200)
    TEL = models.CharField(max_length=200)
class AC_IF(models.Model):
    C_NAME =models.CharField(max_length=200)
    C_NUMBER = models.IntegerField(default=0)
class Item(models.Model):
    NAME = models.CharField(max_length=200)
    PRICE = models.IntegerField(default=0)
class Deal_IF(models.Model):
    AC_ID = models.IntegerField(default=0)
    DEAL_DATE = models.DateTimeField('Date of transaction')
    ITEM_ID = models.IntegerField(default=0)
    BUY_CT = models.IntegerField(default=0)
    BUY_AM = models.IntegerField(default=0)
