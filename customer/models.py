from __future__ import unicode_literals

from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
