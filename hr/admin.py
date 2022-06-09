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

# Register your models here.
