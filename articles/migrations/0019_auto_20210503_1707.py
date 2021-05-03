# Generated by Django 3.1.2 on 2021-05-03 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_tagarticle_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagarticle',
            name='scopes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag', verbose_name='Раздел'),
        ),
    ]
