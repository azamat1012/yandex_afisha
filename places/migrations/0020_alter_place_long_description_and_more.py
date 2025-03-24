# Generated by Django 5.1.7 on 2025-03-24 08:11

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0019_alter_image_options_alter_place_options_image_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Подробное описание места'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, default='', verbose_name='Короткое описание места'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(default='', max_length=150, unique=True, verbose_name='Название места'),
        ),
    ]
