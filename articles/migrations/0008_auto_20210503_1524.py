# Generated by Django 3.1.2 on 2021-05-03 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_tag_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tagarticle',
            old_name='tag_id',
            new_name='scopes',
        ),
    ]
