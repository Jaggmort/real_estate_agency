# Generated by Django 2.2.24 on 2023-04-05 05:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0025_auto_20230405_0826'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Complain',
            new_name='Complaint',
        ),
    ]
