# -*- coding: utf-8 -*-
# pylint: disable=

import logging

from rest_framework import viewsets

from backend import models, serializers

logger = logging.getLogger('backend')

class PeopleViewset(viewsets.ModelViewSet):

    queryset = models.People.objects.all()
    serializer_class = serializers.PeopleSerializer

    def dispatch(self, request, *args, **kwargs):
        logger.info('Dispatching request ...')
        return super().dispatch(request, *args, **kwargs)
