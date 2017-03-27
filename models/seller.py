from __future__ import unicode_literals

from django.db import models


class Seller(models.Model):
    class Meta:
        db_table = "seller"

    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=130)
    mobile = models.CharField(max_length=11, unique=True, null=True)
    email = models.CharField(max_length=30, unique=True, null=True)