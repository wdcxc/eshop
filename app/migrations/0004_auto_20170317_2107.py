# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-03-17 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170317_2100'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productcategorymodel',
            table='product_category',
        ),
    ]
