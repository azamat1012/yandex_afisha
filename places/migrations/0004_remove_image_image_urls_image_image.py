# Generated by Django 5.1.7 on 2025-03-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_remove_place_image_urls_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_urls',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
