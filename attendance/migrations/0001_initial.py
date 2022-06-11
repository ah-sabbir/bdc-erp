# Generated by Django 4.0.5 on 2022-06-11 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterance_date', models.DateField(blank=True, null=True)),
                ('enterance_time', models.TimeField(blank=True, null=True)),
                ('deperature_date', models.DateField(blank=True, null=True)),
                ('deperature_time', models.TimeField(blank=True, null=True)),
                ('entry_card_status', models.CharField(blank=True, choices=[('accept', 'accept'), ('deny', 'deny')], max_length=32)),
                ('comments', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emplyee_attendance', to='hr.employee')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('time_from', models.TimeField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('total_in_hrs', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('approve', 'approve'), ('reject', 'reject')], max_length=32)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LeaveApplicant', to='hr.employee')),
                ('hr_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HRManagerProcess', to='hr.employee')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveApplicationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True)),
                ('comment_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CommentBy', to='hr.employee')),
                ('leave_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LeaveApplicationDetails', to='attendance.leaveapplication')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(blank=True, choices=[('Official', 'Official'), ('Casual', 'Casual')], max_length=32)),
                ('date_from', models.DateField(blank=True, null=True)),
                ('time_from', models.TimeField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('total_in_hrs', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('approve', 'approve'), ('rejected', 'rejected')], max_length=32)),
                ('leave_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LeaveApplication', to='attendance.leaveapplication')),
            ],
        ),
        migrations.CreateModel(
            name='in_out_track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_occure', models.TimeField(blank=True, null=True)),
                ('in_out', models.CharField(blank=True, choices=[('in', 'in'), ('out', 'out')], max_length=32)),
                ('entry_card_status', models.CharField(blank=True, choices=[('accept', 'accept'), ('deny', 'deny')], max_length=32)),
                ('comments', models.TextField(blank=True, null=True)),
                ('atendance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.attendance')),
            ],
        ),
    ]
