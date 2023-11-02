from django.apps import AppConfig


class PagesConfig(AppConfig):
    """
    https://docs.wagtail.org/en/stable/getting_started/integrating_into_django.html
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

    def ready(self):
        if self.is_installed():
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
