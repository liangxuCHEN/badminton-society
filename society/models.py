# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    sexual = models.IntegerField()
    balance = models.FloatField()

class Recharge(models.Model):
    member = models.ForeignKey(Member)
    comment = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    created_at = models.DateTimeField()

class Bill_table(models.Model):
    comment = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField()
    is_pay = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

class Personal_bill(models.Model):
    member = models.ForeignKey(Member)
    bill_table = models.ForeignKey(Bill_table)
    bill_comment = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    created_at = models.DateTimeField()
