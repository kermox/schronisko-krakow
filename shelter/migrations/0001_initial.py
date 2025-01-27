# Generated by Django 3.0.5 on 2020-07-17 15:41

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='imię')),
                ('age', models.PositiveIntegerField(help_text='Wprowadź przybliżony wiek', validators=[django.core.validators.MinValueValidator(0, 'Wiek nie może być <= 0'), django.core.validators.MaxValueValidator(40, 'Wiek nie może być większy od 30')], verbose_name='wiek')),
                ('species', models.CharField(choices=[('dog', 'Pies'), ('cat', 'Kot'), ('other', 'Inny')], max_length=50, verbose_name='gatunek')),
                ('other_species', models.CharField(blank=True, default='', help_text='Wprowadź gatunek', max_length=50, verbose_name='inny gatunek')),
                ('breed', models.CharField(blank=True, default='', max_length=50, verbose_name='rasa')),
                ('gender', models.CharField(choices=[('male', 'Samiec'), ('female', 'Samica')], max_length=6, verbose_name='płeć')),
                ('size', models.CharField(choices=[('small', 'Mały'), ('medium', 'Średni'), ('big', 'Duży')], help_text='Wielkość zwierzęcia', max_length=10, verbose_name='wielkość')),
                ('coat', models.CharField(blank=True, default='', help_text='Określ umaszczenie zwierza', max_length=20, verbose_name='umaszczenie')),
                ('find_place', models.CharField(blank=True, default='', max_length=128, verbose_name='Miejsce gdzie znaleziono zwierzę')),
                ('date_of_adoption', models.DateField(blank=True, null=True, verbose_name='Data adopcji')),
                ('chip_number', models.PositiveIntegerField(blank=True, default=0, verbose_name='numer chip')),
                ('identification_number', models.PositiveIntegerField(blank=True, default=0, verbose_name='identyfikator')),
                ('medical_information', models.TextField(blank=True, default='', verbose_name='Stan zdrowia')),
                ('documents', models.FileField(blank=True, default='', upload_to='animal_documents/', verbose_name='dokumenty')),
                ('additional_information', models.CharField(blank=True, default='', max_length=250, verbose_name='dodatkowe informacje')),
                ('photo', models.ImageField(upload_to='animal_photos/', verbose_name='zdjęcie')),
            ],
        ),
        migrations.CreateModel(
            name='PetOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='imię')),
                ('second_name', models.CharField(max_length=50, verbose_name='nazwisko')),
                ('adress', models.CharField(help_text='Podaj adress zamieszkania', max_length=150, verbose_name='adress')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('phone_number', models.PositiveIntegerField(verbose_name='numer telefonu')),
                ('adopting_agreement', models.FileField(upload_to='agreements/', verbose_name='umowa adopcyjna')),
                ('animal', models.ForeignKey(help_text='Wybierz zwierzę które chcesz zaadaptować', on_delete=django.db.models.deletion.PROTECT, to='shelter.Animal', verbose_name='adoptowane zwiere')),
            ],
        ),
    ]
