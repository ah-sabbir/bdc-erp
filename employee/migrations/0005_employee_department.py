# Generated by Django 4.0.5 on 2022-06-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_rename_role_employee_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(blank=True, max_length=3, verbose_name='Department'),
        ),
    ]