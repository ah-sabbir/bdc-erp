# Generated by Django 4.0.5 on 2022-06-08 11:07

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_joined_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Role',
            new_name='role',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employee_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, max_length=255, verbose_name='Designation'),
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=125, verbose_name='First Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2022, 6, 8, 11, 7, 32, 210431, tzinfo=utc), max_length=125, verbose_name='Last Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='section',
            field=models.CharField(choices=[('S', 'Sale'), ('O', 'Operation')], default=0, max_length=2, verbose_name='Section'),
            preserve_default=False,
        ),
    ]