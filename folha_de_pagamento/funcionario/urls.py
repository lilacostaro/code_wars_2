from django.urls import path

from . import views

urlpatterns = [
    path('funcionarios/', views.employeesList, name='funcionarios_list'),
    path('funcionarios/<str:matricula>/', views.employeeInfo, name='employee_info'),
    path('funcionarios/add', views.addEmployee, name='add_employee'),
]