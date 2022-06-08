import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
# from utils.baseModel import  SoftDeleteModel


class Employee(AbstractBaseUser):
    """
    Employee
    """

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

    id = models.AutoField("Id", auto_created=True, primary_key=True, serialize=False)
    role = models.CharField("Role", max_length=20, choices=role_type_choices, null=False)
    user_name = models.CharField("Employee Id", max_length=255, unique=True, blank=False)
    USERNAME_FIELD = "user_name"
    first_name = models.CharField("First Name", max_length=125)
    last_name = models.CharField("Last Name", max_length=125)
    gender = models.CharField("Gender", choices=GENDERS, max_length=2, null=False)
    email = models.CharField("Email", max_length=255, unique=True)
    phone = models.CharField("Phone", max_length=255, null=False)
    image_path = models.CharField("Profile Image Path", max_length=1000, null=False, blank=True)
    department = models.CharField("Department", max_length=3, null=False, blank=True, choices=working_departments)
    designation = models.CharField("Designation", max_length=255, null=False, blank=True)
    section = models.CharField("Section", max_length=2, null=False, choices=working_sections)
    joined_date = models.DateTimeField(
        default = timezone.now,
        verbose_name = "Join Date",
        null=False,
        blank=False
    )
    # pwd_reset_time = models.DateTimeField(
    #     default=timezone.now,
    #     verbose_name="Change password time",
    #     help_text="Change password time",
    #     null=True,
    #     blank=True,
    # )

    # create_by = models.CharField(
    #     null=True, blank=True, verbose_name="created_by", help_text="Created By", max_length=50
    # )
    # update_by = models.CharField(
    #     null=True, blank=True, verbose_name="Updated_by", help_text="Updated By", max_length=50
    # )
    # create_at = models.DateTimeField(
    #     auto_now_add=True,
    #     verbose_name="created_at",
    #     help_text="Ceared at",
    #     null=True,
    #     blank=True,
    # )
    # update_at = models.DateTimeField(
    #     auto_now=True, verbose_name="Updated_at", help_text="Updated at", null=True, blank=True
    # )

    # is_deleted = models.BooleanField(
    #     default=False, verbose_name="delete marker", help_text="delete marker"
    # )

    # is_activate = models.BooleanField(
    #     default=True, verbose_name="Status: 1 enabled, 0 disabled", help_text="Status: 1 enabled, 0 disabled"
    # )

    # dept = models.ForeignKey(
    #     Dept, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Department"
    # )
    # position = models.ForeignKey(
    #     Position, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Position"
    # )
    # roles = models.ManyToManyField(Role, blank=True, verbose_name="Employee Role")

    # objects = BaseUserManager()

    class Meta:
        managed = True
        verbose_name = "Employee Info"
        verbose_name_plural = verbose_name
        unique_together = ( "phone", "email")
        ordering = ["id"]

    def __str__(self):
        return self.user_name




class Attendance(models.Model):
    Employee = models.ForeignKey(Employee, primary_key=True, on_delete=models.CASCADE,)
    isPresent = models.BooleanField(default=False, null = False, blank=False)
    Date = models.DateTimeField(auto_created = True, null=False, blank= False)
    Comments = models.CharField("Comments", max_length=200,null=True)
    added_by = models.CharField("Entry By", max_length=100, null=False, blank=False)

    class Meta:
        # managed = True
        verbose_name = "Attendance"
        verbose_name_plural = verbose_name
        ordering = ["Date"]

    def __str__(self):
        return self.Date




# class Position(SoftDeleteModel):
#     """
#     EMPLOYEE POSITION
#     """
#     position_id = models.AutoField("POSITION ID", primary_key=True)
#     position_name = models.CharField("POSITION NAME", max_length=32, unique=True)
#     description = models.CharField("DESCRIPTION", max_length=50, blank=True, null=True)

#     class Meta:
#         managed = True
#         verbose_name = "Position/Position"
#         verbose_name_plural = verbose_name
#         ordering = ["position_id"]

#     def __str__(self):
#         return self.position_name

# class Dept(SoftDeleteModel):
#     """
#     EMPLOYEE DEPARTMENT 
#     """
#     dept_id = models.AutoField("DEPARTEMENT ID", primary_key=True)
#     dept_name = models.CharField("DEPARTMENT NAME", max_length=255)
#     dept_sort = models.IntegerField("SORT", default=999)

#     class Meta:
#         managed = True
#         verbose_name = "DEPARTMENT"
#         verbose_name_plural = verbose_name
#         ordering = ["dept_id"]

#     def __str__(self):
#         return self.dept_name

# class Role(SoftDeleteModel):
#     """
#     Employee Role
#     """

#     data_type_choices = (
#         ("All", "All"),
#         ("Admin", "Admin"),
#         ("Project Manager", "Project Manager"),
#         ("Team Leader", "Team Leader"),
#         ("Leader", "Leader"),
#         ("Member", "Member"),
#     )
#     role_id = models.AutoField("ROLE ID", primary_key=True)
#     role_name = models.CharField("Role Name", max_length=255, unique=True)
#     role_level = models.IntegerField("Role Level", null=True)
#     description = models.CharField("Description ", max_length=255, blank=True, null=True)
#     data_scope = models.CharField(
#         "data permission",
#         max_length=255,
#         choices=data_type_choices,
#         default="Member",
#         null=True,
#         blank=True,
#     )

#     depts = models.ManyToManyField(Dept, blank=False, verbose_name="role department association")

#     class Meta:
#         managed = True
#         verbose_name = "Role"
#         verbose_name_plural = verbose_name
#         ordering = ["role_id"]

#     def __str__(self):
#         return self.role_name