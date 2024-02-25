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

# from django.views.decorators.cache import cache_page  # , never_cache
# from django.views.generic import TemplateView
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

from pages.views import TagView


logger = logging.getLogger(__name__)

from django.contrib.sitemaps import Sitemap as DjangoSitemap


class Sitemap(DjangoSitemap):
    def __init__(self, request=None):
        self.request = request

    def location(self, obj):
        return obj.get_full_url(self.request)

    def lastmod(self, obj):
        # fall back on latest_revision_created_at if last_published_at is null
        # (for backwards compatibility from before last_published_at was added)
        return obj.last_published_at or obj.latest_revision_created_at

    def get_wagtail_site(self):
        from wagtail.models import Site

        site = Site.find_for_request(self.request)
        if site is None:
            return Site.objects.select_related("root_page").get(is_default_site=True)
        return site

    def items(self):
        """
        return (
            self.get_wagtail_site()
            .root_page.get_descendants(inclusive=True)
            .live()
            .public()
            .order_by("path")
            .defer_streamfields()
            .specific()
        )
        """
        from wagtail.models import Page
        return Page.objects.live()

    def _urls(self, page, protocol, domain):
        urls = []
        last_mods = set()

        for item in self.paginator.page(page).object_list.iterator():
            url_info_items = item.get_sitemap_urls(self.request)

            for url_info in url_info_items:
                urls.append(url_info)
                last_mods.add(url_info.get("lastmod"))

        # last_mods might be empty if the whole site is private
        if last_mods and None not in last_mods:
            self.latest_lastmod = max(last_mods)
        return urls

sitemaps = {
    "pages": Sitemap,
}

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, ),
    path(r"cms/", include(wagtailadmin_urls)),
    path(r"documents/", include(wagtaildocs_urls)),
    path(r"pages/", include(wagtail_urls)),
    path(r"tags/<str:slug>/", TagView.as_view(), name="tag-detail"),
]
