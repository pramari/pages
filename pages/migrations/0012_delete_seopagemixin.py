# Generated by Django 4.2.7 on 2024-01-21 07:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0011_remove_homepage_search_image_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SEOPageMixin",
        ),
    ]
