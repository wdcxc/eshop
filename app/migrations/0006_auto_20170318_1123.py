# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-03-18 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_productcategorymodel_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategorymodel',
            name='grade',
            field=models.IntegerField(default=1),
        ),
    ]
