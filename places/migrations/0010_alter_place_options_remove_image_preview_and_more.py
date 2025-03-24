# Generated by Django 5.1.7 on 2025-03-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_image_preview_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['my_order']},
        ),
        migrations.RemoveField(
            model_name='image',
            name='preview',
        ),
        migrations.AddField(
            model_name='place',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
