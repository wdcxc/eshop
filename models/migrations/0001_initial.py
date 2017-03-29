# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=130)),
                ('loginTime', models.DateTimeField()),
                ('grade', models.IntegerField(default=999)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='CarouselModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('show', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=1)),
                ('imgUrl', models.URLField()),
                ('linkUrl', models.URLField()),
                ('addTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'index_carousel',
            },
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=130)),
                ('mobile', models.CharField(max_length=11, null=True, unique=True)),
                ('email', models.CharField(max_length=30, null=True, unique=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentId', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=1)),
                ('grade', models.IntegerField(default=1)),
                ('show', models.BooleanField(default=True)),
                ('addTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'product_category',
            },
        ),
        migrations.CreateModel(
            name='ShoppingGuideChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('addTime', models.DateTimeField(auto_now_add=True)),
                ('addAdminId', models.IntegerField()),
                ('show', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'shoppingguide_channel',
            },
        ),
        migrations.CreateModel(
            name='ShoppingGuideProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentId', models.IntegerField()),
                ('productId', models.IntegerField()),
                ('addTime', models.DateTimeField(auto_now_add=True)),
                ('addAdminId', models.IntegerField()),
                ('show', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'shoppingguide_product',
            },
        ),
        migrations.CreateModel(
            name='ShoppingGuideSubchannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parentId', models.IntegerField()),
                ('addTime', models.DateTimeField(auto_now_add=True)),
                ('addAdminId', models.IntegerField()),
                ('show', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'shoppingguide_subchannel',
            },
        ),
    ]
