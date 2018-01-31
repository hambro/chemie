# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 19:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Tittel')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Dato')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('register_startdate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Påmeldingen åpner')),
                ('register_deadline', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Påmeldingsfrist')),
                ('deregister_deadline', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Avmeldingsfrist')),
                ('location', models.TextField(verbose_name='Sted')),
                ('description', models.TextField(verbose_name='Beskrivelse')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='events', verbose_name='Bilde')),
                ('sluts', models.PositiveSmallIntegerField(default=100, verbose_name='Antall plasser')),
                ('payment_information', models.TextField(max_length=500, verbose_name='Betalingsinformasjon')),
                ('price_member', models.PositiveSmallIntegerField(default=0, verbose_name='Pris, medlem')),
                ('price_not_member', models.PositiveSmallIntegerField(default=0, verbose_name='Pris, ikke-medlem')),
                ('price_companion', models.PositiveSmallIntegerField(default=0, verbose_name='Pris for følge')),
                ('companion', models.BooleanField(default=False, verbose_name='Følge')),
                ('sleepover', models.BooleanField(default=False, verbose_name='Overnatting')),
                ('night_snack', models.BooleanField(default=False, verbose_name='Nattmat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Confirmed'), (2, 'Waiting')], default=2)),
                ('payment_status', models.BooleanField(default=False, verbose_name='Betalt')),
                ('sleepover', models.BooleanField(default=False, verbose_name='Overnatting')),
                ('night_snack', models.BooleanField(default=False, verbose_name='Nattmat')),
                ('companion', models.CharField(blank=True, help_text='Navn på ekstern person. Ønske om bordkavaler sendes til festkom.', max_length=40, null=True, verbose_name='Navn på følge')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Limitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(choices=[(1, 'Første'), (2, 'Andre'), (3, 'Tredje'), (4, 'Fjerde'), (5, 'Femte'), (6, 'Ferdig')], verbose_name='Klassetrinn')),
                ('slots', models.PositiveSmallIntegerField(default=100, verbose_name='Antall plasser')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_message', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(through='events.EventRegistration', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='limitations',
            field=models.ManyToManyField(blank=True, to='events.Limitation'),
        ),
        migrations.AlterUniqueTogether(
            name='eventregistration',
            unique_together=set([('event', 'user')]),
        ),
    ]