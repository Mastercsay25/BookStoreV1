# Generated by Django 3.0.7 on 2020-07-09 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
