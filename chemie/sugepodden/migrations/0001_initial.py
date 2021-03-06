# Generated by Django 2.2.10 on 2020-10-05 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200, verbose_name='beskrivelse')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='sugepodden', verbose_name='Bilde')),
                ('published', models.BooleanField(default=True, verbose_name='Publisert')),
                ('url', models.URLField(default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
