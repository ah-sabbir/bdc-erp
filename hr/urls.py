from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees, name='employees'),
    # path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    # path('departments/', views.departments, name='departments'),
    # path('departments/<int:department_id>/', views.department_detail, name='department_detail'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/edit/', views.profile_edit, name='profile_edit'),
    # path('profile/change_password/', views.change_password, name='change_password'),
]