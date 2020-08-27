# Generated by Django 3.1 on 2020-08-20 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityimage',
            name='images',
            field=models.FileField(upload_to='Community/'),
        ),
        migrations.CreateModel(
            name='CommunityPostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='community/post/')),
                ('communitypost', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='community.communitypost')),
            ],
        ),
    ]