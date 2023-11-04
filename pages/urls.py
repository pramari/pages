#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ts=4 et sw=4 sts=4
# pylint: disable=invalid-name

"""
urls.py.

Route traffic to code.
"""

import logging


from django.urls import path
from django.conf.urls import include
from django.views.decorators.cache import cache_page  # , never_cache
from django.views.generic import TemplateView


logger = logging.getLogger(__name__)


if settings.WAGTAIL:
    from wagtail import urls as wagtail_urls
    from wagtail.admin import urls as wagtailadmin_urls
    from wagtail.documents import urls as wagtaildocs_urls
    from wagtail.contrib.sitemaps.views import sitemap

    from pages.models import HomePage, HomeIndexPage, MethodPage

    urlpatterns += [
        path("sitemap.xml", sitemap),
        path(r"cms/", include(wagtailadmin_urls)),
        path(r"documents/", include(wagtaildocs_urls)),
        path(r"pages/", include(wagtail_urls)),
    ]
