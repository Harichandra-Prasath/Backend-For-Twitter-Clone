# Generated by Django 4.2 on 2023-04-09 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0007_remove_bookmarks_bookmarked_in_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bookmarks',
        ),
    ]
