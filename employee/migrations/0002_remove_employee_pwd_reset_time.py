# Generated by Django 4.0.5 on 2022-06-08 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='pwd_reset_time',
        ),
    ]
