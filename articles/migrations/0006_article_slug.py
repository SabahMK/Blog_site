# Generated by Django 2.2.7 on 2019-12-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20191227_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='slug'),
        ),
    ]
