# -*- coding: utf-8 -*-
# pylint: disable=

from django.db import models

class People(models.Model):
    
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
