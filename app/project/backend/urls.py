# -*- coding: utf-8 -*-
# pylint: disable=

from rest_framework.routers import DefaultRouter

from backend import views

router = DefaultRouter(trailing_slash=False)

router.register('people', views.PeopleViewset, 'people')

urlpatterns = router.urls
