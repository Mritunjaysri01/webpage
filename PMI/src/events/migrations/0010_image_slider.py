# Generated by Django 3.1 on 2020-08-19 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20200820_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='slider',
            field=models.BooleanField(default=False),
        ),
    ]