# Generated by Django 2.2.24 on 2023-03-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230331_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='own_flats',
            field=models.ManyToManyField(null=True, related_name='owned_flats', to='property.Flat'),
        ),
    ]
