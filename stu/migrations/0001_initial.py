# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2023-08-23 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('parent_id', models.IntegerField()),
                ('first_letter', models.CharField(max_length=10)),
                ('level', models.IntegerField()),
            ],
            options={
                'db_table': 'area',
                'managed': False,
            },
        ),
    ]
