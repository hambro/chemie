# Generated by Django 2.1.5 on 2019-02-04 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_officeapplication_access_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundsapplication',
            name='receipt',
        ),
    ]
