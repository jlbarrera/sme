from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from core.models import Employee
from django.contrib.auth.models import User
from multitenant.models import Tenant
from django.http import HttpResponseRedirect 

class EmployeeList(ListView):    
    
    def get_queryset(self):
        return Employee.tenant_objects.all()
    
class EmployeeDetail(DetailView):
    
    def get_queryset(self):
        return Employee.tenant_objects.all()
    
class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name']    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        user = User.objects.filter(username=form.instance.name)
        if not user:        
            user = User(username=form.instance.name, password="123456")
            user.save()        
        tenant = Tenant(name=form.instance.name)
        tenant.save()
        employee = Employee(name=form.instance.name, user=user, tenant=tenant)
        employee.save()                
        return HttpResponseRedirect(reverse_lazy('employees-list'))

class EmployeeUpdate(UpdateView):    
    fields = ['name']
    success_url=reverse_lazy('employees-list')
    
    def get_queryset(self):
        return Employee.tenant_objects.all()

class EmployeeDelete(DeleteView):
    success_url = reverse_lazy('employees-list')
    
    def get_queryset(self):
        return Employee.tenant_objects.all()