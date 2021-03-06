# Generated by Django 2.2.7 on 2020-01-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20191230_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified on'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Published on'),
        ),
    ]
