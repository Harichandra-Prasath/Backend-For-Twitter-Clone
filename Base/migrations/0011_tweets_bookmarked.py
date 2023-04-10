# Generated by Django 4.2 on 2023-04-09 05:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Base', '0010_delete_bookmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='bookmarked',
            field=models.ManyToManyField(null=True, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]
