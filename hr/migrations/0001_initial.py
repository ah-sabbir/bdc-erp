# Generated by Django 4.0.5 on 2022-06-11 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=255, verbose_name='Department Name')),
                ('department_code', models.CharField(max_length=255, verbose_name='Department Code')),
                ('department_description', models.TextField(max_length=255, verbose_name='Department Description')),
                ('department_head', models.CharField(max_length=255, verbose_name='Department Head')),
                ('department_head_phone', models.CharField(max_length=255, verbose_name='Department Head Phone')),
                ('department_head_email', models.EmailField(max_length=254, verbose_name='Department Head Email')),
                ('department_head_picture', models.FileField(blank=True, null=True, upload_to='profile_images/%Y/%m/%d')),
                ('revenue', models.IntegerField(default=None, verbose_name='Revenue')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Department',
                'ordering': ['department_code'],
                'managed': True,
                'unique_together': {('department_code', 'department_name')},
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('employee_id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='Employee Id')),
                ('first_name', models.CharField(max_length=125, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=125, verbose_name='Last Name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2, verbose_name='Gender')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('picture', models.FileField(blank=True, null=True, upload_to='profile_images/%Y/%m/%d')),
                ('date_of_birth', models.DateField(verbose_name='Birth Date')),
                ('role', models.CharField(choices=[('All', 'All'), ('Admin', 'Admin'), ('Editor', 'Editor'), ('Member', 'Member')], max_length=20, verbose_name='Role')),
                ('age', models.IntegerField(default=None, verbose_name='Age')),
            ],
            options={
                'verbose_name': 'Employee Info',
                'verbose_name_plural': 'Employee Info',
                'ordering': ['employee_id'],
                'managed': True,
                'unique_together': {('phone', 'email', 'employee_id')},
            },
        ),
        migrations.CreateModel(
            name='ServiceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('office_name', models.CharField(blank=True, max_length=255, null=True)),
                ('section', models.CharField(choices=[('S', 'Sale'), ('O', 'Operation')], max_length=2, verbose_name='Section')),
                ('date_from', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EmployeeDipartment', to='hr.department')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ServiceHistory', to='hr.employee')),
            ],
        ),
    ]
