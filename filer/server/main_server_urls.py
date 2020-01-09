# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<path>.*)$', views.serve_protected_file),
]
