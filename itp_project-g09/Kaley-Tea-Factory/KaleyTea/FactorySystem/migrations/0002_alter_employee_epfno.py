# Generated by Django 3.2.6 on 2021-10-08 08:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactorySystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='epfNo',
            field=models.IntegerField(null=True, unique=True, validators=[django.core.validators.RegexValidator(code='EPF No is invalid', message='EPF No can only contain positive numbers', regex='^[0-9]*$')]),
        ),
    ]