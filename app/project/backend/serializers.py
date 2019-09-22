# -*- coding: utf-8 -*-
# pylint: disable=

from rest_framework import serializers

from backend import models


class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.People
        fields = '__all__'
