from django.db import models
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from django.utils.translation import gettext_lazy as _

from wagtailmetadata.models import MetadataPageMixin


class SEOPageMixin(index.Indexed, MetadataPageMixin):
    search_engine_index = models.BooleanField(
        blank=False,
        null=False,
        default=True,
        verbose_name=_("Allow search engines to index this page?"),
    )

    search_engine_changefreq = models.CharField(
        max_length=25,
        choices=[
            ("always", _("Always")),
            ("hourly", _("Hourly")),
            ("daily", _("Daily")),
            ("weekly", _("Weekly")),
            ("monthly", _("Monthly")),
            ("yearly", _("Yearly")),
            ("never", _("Never")),
        ],
        blank=True,
        null=True,
        verbose_name=_("Search Engine Change Frequency (Optional)"),
        help_text=_(
            "How frequently the page is likely to change? (Leave blank for default)"
        ),
    )

    search_engine_priority = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name=_("Search Engine Priority (Optional)"),
        help_text=_(
            "The priority of this URL relative to other URLs on your site. Valid values range from 0.0 to 1.0. (Leave blank for default)"
        ),
    )

    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel("search_engine_index"),
                FieldPanel("search_engine_changefreq"),
                FieldPanel("search_engine_priority"),
            ],
            _("Search Engine Indexing"),
        ),
    ]

    @property
    def lastmod(self):
        return self.last_published_at or self.latest_revision_created_at

    def get_sitemap_urls(self):
        sitemap = super().get_sitemap_urls()
        if self.search_engine_index:
            url_item = {"location": self.full_url, "lastmod": self.lastmod}
            if self.search_engine_changefreq:
                url_item["changefreq"] = self.search_engine_changefreq
            if self.search_engine_priority:
                url_item["priority"] = self.search_engine_priority
            sitemap.append(url_item)
            return sitemap
        else:
            return []
