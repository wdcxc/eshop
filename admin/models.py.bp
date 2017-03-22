from __future__ import unicode_literals

from django.db import models

class AdminModel(models.Model):
    class Meta:
        db_table = "admin"

    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=130)

