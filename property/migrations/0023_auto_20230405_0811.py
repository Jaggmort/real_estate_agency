# Generated by Django 2.2.24 on 2023-04-05 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0022_auto_20230404_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
