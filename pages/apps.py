from django.apps import AppConfig


class PagesConfig(AppConfig):
    """
    https://docs.wagtail.org/en/stable/getting_started/integrating_into_django.html
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

    def ready(self):
        if not self.apps.is_installed("wagtail"):
            """
            'wagtail.contrib.forms',
            'wagtail.contrib.redirects',
            'wagtail.embeds',
            'wagtail.sites',
            'wagtail.users',
            'wagtail.snippets',
            'wagtail.documents',
            'wagtail.images',
            'wagtail.search',
            'wagtail.admin',
            'wagtail',

            'modelcluster',
            'taggit',
            """
            raise Exception
        from .signals import publish_to_mastodon
        from wagtail.signals import page_published

        page_published.connect(publish_to_mastodon)


