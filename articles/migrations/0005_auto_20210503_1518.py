# Generated by Django 3.1.2 on 2021-05-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210503_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagarticle',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
