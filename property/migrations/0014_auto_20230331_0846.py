# Generated by Django 2.2.24 on 2023-03-31 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner',
            field=models.CharField(max_length=200, verbose_name='ФИО владельца'),
        ),
    ]
