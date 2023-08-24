# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Area(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    first_letter = models.CharField(max_length=10)
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'area'
