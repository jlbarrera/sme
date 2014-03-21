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
    fields = ['name', 'email']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EmployeeCreate, self).form_valid(form)

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'email']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees')