# Generated by Django 5.0 on 2023-12-22 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pts', '0007_passport_pts_passport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='pts',
            options={'ordering': ['-publish_date'], 'verbose_name': 'Pets', 'verbose_name_plural': 'Pets'},
        ),
        migrations.AddField(
            model_name='pts',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='pts',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cats', to='pts.category'),
        ),
    ]