# Generated by Django 3.0.7 on 2020-07-10 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_billingaddress_saved_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='saved_date',
            new_name='auto_saved_date',
        ),
    ]