# Generated by Django 3.1.2 on 2021-05-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20210503_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='is_main',
        ),
        migrations.AddField(
            model_name='tagarticle',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
