# Generated by Django 3.1 on 2020-08-19 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
        ('events', '0002_auto_20200820_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Enter The Title', max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('Category', models.ManyToManyField(to='events.Category')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.author')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='content',
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='Enter The Title', max_length=100),
        ),
        migrations.CreateModel(
            name='EventContentView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.eventcontent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
