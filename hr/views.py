from django.shortcuts import render
# import employee model
from hr.models import Employee
# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


#  view to show all employees
def employees(request):
    employees = Employee.objects.all()
    print (employees)
    return render(request, 'Employee/index.html', {'employees': employees})
