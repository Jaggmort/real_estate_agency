# Generated by Django 2.2.24 on 2023-04-04 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20230331_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='own_flats',
            new_name='flats',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]
