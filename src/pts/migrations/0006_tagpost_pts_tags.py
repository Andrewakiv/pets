# Generated by Django 5.0 on 2023-12-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pts', '0005_alter_pts_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=225)),
                ('slug', models.SlugField(max_length=225, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='pts',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='pts.tagpost'),
        ),
    ]
