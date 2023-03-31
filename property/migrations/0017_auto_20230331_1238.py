# Generated by Django 2.2.24 on 2023-03-31 09:38

from django.db import migrations


def fill_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(owner=flat.owner,
                                    owners_phonenumber=flat.owners_phonenumber,
                                    owner_pure_phone=flat.owner_pure_phone,
                                    )

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20230331_1238'),
    ]

    operations = [
        migrations.RunPython(fill_owners)
    ]
