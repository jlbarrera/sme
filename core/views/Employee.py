from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from core.models import Employee 

class EmployeeList(ListView):
    model = Employee

class EmployeeDetail(DetailView):
    model = Employee
    
class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name']

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees')