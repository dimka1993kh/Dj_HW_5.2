# Generated by Django 3.1.2 on 2021-05-03 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_tag_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='main',
        ),
    ]
