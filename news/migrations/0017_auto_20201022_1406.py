# Generated by Django 3.0.5 on 2020-10-22 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20201022_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Topic', verbose_name='wątek'),
        ),
    ]
