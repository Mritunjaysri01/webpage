# Generated by Django 3.1 on 2020-08-19 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='categories',
            new_name='Category',
        ),
    ]