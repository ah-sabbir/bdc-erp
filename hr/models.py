import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
# from utils.baseModel import  SoftDeleteModel
from datetime import timedelta
from datetime import datetime
from datetime import date
from datetime import time
import datetime as dt


working_sections = [
    ("S","Sale"),
    ("O", "Operation")
]

working_departments = [
    ("HR","Human Resource"),
    ("DEV", "Developement"),
    ("VC", "Vitual and Creative Designs"),
    ("BS","Bussiness Support Executives")
]



GENDERS = [
("M","Male"),
("F", "Female")
]

role_type_choices = (
("All", "All"),
("Admin", "Admin"),
("Editor","Editor"),
("Member", "Member"),
)

class Employee(AbstractBaseUser):
    """
    Employee
    """

    # id = models.AutoField("Id", auto_created=True, primary_key=True, serialize=False)
    employee_id = models.CharField("Employee Id", max_length=255, primary_key=True,  unique=True, blank=False)
    USERNAME_FIELD = 'employee_id'
    first_name = models.CharField("First Name", max_length=125)
    last_name = models.CharField("Last Name", max_length=125)
    gender = models.CharField("Gender", choices=GENDERS, max_length=2, null=False)
    email = models.EmailField("Email", unique=True)
    phone = models.CharField("Phone", max_length=255, null=False)
    picture = models.FileField(upload_to='profile_images/%Y/%m/%d',blank=True, null=True) 
    date_of_birth = models.DateField("Birth Date", null=False)
    role = models.CharField("Role", max_length=20, choices=role_type_choices, null=False)
    age = models.IntegerField(default=None, verbose_name='Age')




    class Meta:
        managed = True
        verbose_name = "Employee Info"
        verbose_name_plural = verbose_name
        unique_together = ( "phone", "email","employee_id")
        ordering = ["employee_id"]

    def __str__(self):
        return self.employee_id
    
    def __save__(self, *args, **kwargs):
        self.age = (datetime.date.today() - self.date_of_birth).days // 365


# create a class for departments
class Department(models.Model):
    department_name = models.CharField("Department Name", max_length=255, null=False, blank=False)
    department_code = models.CharField("Department Code", max_length=255, null=False, blank=False)
    department_description = models.TextField("Department Description", max_length=255, null=False, blank=False)
    department_head = models.CharField("Department Head", max_length=255, null=False, blank=False)
    department_head_phone = models.CharField("Department Head Phone", max_length=255, null=False, blank=False)
    department_head_email = models.EmailField("Department Head Email", null=False, blank=False)
    department_head_picture = models.FileField(upload_to='profile_images/%Y/%m/%d',blank=True, null=True)
    revenue = models.IntegerField(default=None, verbose_name='Revenue')

    class Meta:
        managed = True
        verbose_name = "Department"
        verbose_name_plural = verbose_name
        unique_together = ( "department_code", "department_name")
        ordering = ["department_code"]

    def __str__(self):
        return self.department_name


class ServiceHistory(models.Model):
    employee = models.ForeignKey(Employee, blank=True, null=True,related_name='ServiceHistory',on_delete=models.CASCADE)
    designation= models.CharField(max_length=255, blank=True, null=True)
    office_name  = models.CharField(max_length=255, blank=True, null=True)
    department = models.ForeignKey(Department, blank=True, null=True,related_name='EmployeeDipartment',on_delete=models.CASCADE)
    section = models.CharField("Section", max_length=2, null=False, choices=working_sections)
    date_from =  models.DateField( blank=True, null=True)
    date_from = models.DateField( blank=True, null=True)






# class Attendance(models.Model):
#     Employee = models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE,)
#     isPresent = models.BooleanField(default=False, null = False, blank=False)
#     Date = models.DateTimeField(auto_created = True, null=False, blank= False)
#     Comments = models.CharField("Comments", max_length=200,null=True)
#     added_by = models.CharField("Entry By", max_length=100, null=False, blank=False)

#     class Meta:
#         # managed = True
#         verbose_name = "Attendance"
#         verbose_name_plural = verbose_name
#         ordering = ["Date"]

#     def __str__(self):
#         return self.Date


