# Generated by Django 4.2.7 on 2024-01-05 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("pages", "0008_alter_homeindexpage_options_alter_homepage_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="search_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Search image",
            ),
        ),
        migrations.AddField(
            model_name="methodpage",
            name="search_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Search image",
            ),
        ),
    ]
