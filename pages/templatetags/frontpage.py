import logging

from django import template

logger = logging.getLogger(__name__)
register = template.Library()

@register.simple_tag
def tiles(tag: str):
    try:
        from .models import HomePage
    except ImportError:
        logger.error("Pages not installed.")
        return
    return HomePage.objects.filter(frontpage=True)
