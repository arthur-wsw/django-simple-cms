# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_simple_cms.urls import urlpatterns as django_simple_cms_urls

urlpatterns = [
    url(r'^', include(django_simple_cms_urls, namespace='django_simple_cms')),
]
