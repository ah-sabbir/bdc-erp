from django.contrib import admin
from hr.models import *

class ServiceHistoryInline(admin.TabularInline):
    model = ServiceHistory
    extra = 1  

class EmployeeAdmin(admin.ModelAdmin):
    model   = Employee
    inlines = [ServiceHistoryInline]
    
    list_display = ("employee_id", "first_name","last_name","gender","email","phone")

admin.site.register(Employee, EmployeeAdmin) 

class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ('id', 'department_name', 'department_code', 'department_description', 'department_head', 'department_head_phone', 'department_head_email', 'department_head_picture', 'revenue')
# DepartmentAdmin
admin.site.register(Department, DepartmentAdmin)
# Register your models here.
