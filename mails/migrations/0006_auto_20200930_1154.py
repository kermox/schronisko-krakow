# Generated by Django 3.0.5 on 2020-09-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0005_auto_20200924_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_body', models.TextField(blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='EmailAddresses',
            new_name='EmailBase',
        ),
        migrations.DeleteModel(
            name='Mail',
        ),
    ]
