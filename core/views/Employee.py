from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from core.models import Employee 

class EmployeeList(ListView):    
    queryset = Employee.tenant_objects.all()

class EmployeeDetail(DetailView):
    queryset = Employee.tenant_objects.all()
    
class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'email']
    success_url = reverse_lazy('employees-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EmployeeCreate, self).form_valid(form)

class EmployeeUpdate(UpdateView):
    queryset = Employee.tenant_objects.all()
    fields = ['name', 'email']
    success_url=reverse_lazy('employees-list')

class EmployeeDelete(DeleteView):
    queryset = Employee.tenant_objects.all()
    success_url = reverse_lazy('employees-list')