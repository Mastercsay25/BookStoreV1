# Generated by Django 3.0.7 on 2020-07-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_picture/default.png', upload_to='profile_picture'),
        ),
    ]
