# Generated by Django 2.2.10 on 2020-09-23 07:01

import ckeditor.fields
from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobAdvertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Stilling')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Beskrivelse')),
                ('is_published', models.BooleanField(default=True, verbose_name='Er synlig')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveSmallIntegerField(choices=[(1, 'Bioteknologi'), (2, 'Organisk kjemi'), (3, 'Anvendt teoretisk kjemi'), (4, 'Analytisk kjemi'), (5, 'Kjemisk prosessteknologi'), (6, 'Materialkjemi og energiteknologi')], unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Navn på intervjuet')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Intervjuet')),
                ('picture', sorl.thumbnail.fields.ImageField(upload_to='corporate', verbose_name='Bilde')),
                ('is_published', models.BooleanField(default=True, verbose_name='Er synlig')),
                ('specializations', models.ManyToManyField(blank=True, to='corporate.Specialization', verbose_name='Aktuelle retninger')),
            ],
        ),
    ]