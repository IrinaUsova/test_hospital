# Generated by Django 2.2.4 on 2019-08-27 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190827_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='address',
            new_name='adress',
        ),
    ]
