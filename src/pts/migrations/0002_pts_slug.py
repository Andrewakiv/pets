# Generated by Django 5.0 on 2023-12-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pts',
            name='slug',
            field=models.SlugField(blank=True, default=' ', max_length=225),
        ),
    ]
