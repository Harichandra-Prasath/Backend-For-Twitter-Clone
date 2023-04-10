# Generated by Django 4.2 on 2023-04-06 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Base', '0002_alter_comments_commented_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL),
        ),
    ]
