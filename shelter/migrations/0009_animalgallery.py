# Generated by Django 3.0.5 on 2020-08-12 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0008_animal_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to='')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='photos', to='shelter.Animal')),
            ],
        ),
    ]
