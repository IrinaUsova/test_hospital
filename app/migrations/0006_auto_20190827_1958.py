# Generated by Django 2.2.4 on 2019-08-27 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_doctor_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='experience',
            new_name='position',
        ),
    ]