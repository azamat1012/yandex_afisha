# Generated by Django 5.1.7 on 2025-03-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0016_alter_place_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]
