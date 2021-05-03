# Generated by Django 3.1.2 on 2021-05-03 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20210503_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagarticle',
            name='article_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AlterField(
            model_name='tagarticle',
            name='scopes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag'),
        ),
    ]
