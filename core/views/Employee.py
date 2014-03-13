from django.views.generic import ListView
from core.models import Employee

class EmployeeList(ListView):
    model = Employee