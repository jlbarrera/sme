from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from core.models import Customer

class CustomerList(ListView):    
    queryset = Customer.tenant_objects.all()

class CustomerDetail(DetailView):
    queryset = Customer.tenant_objects.all()
    
class CustomerCreate(CreateView):
    model = Customer
    fields = ['name', 'email']
    success_url = reverse_lazy('customers-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CustomerCreate, self).form_valid(form)

class CustomerUpdate(UpdateView):
    queryset = Customer.tenant_objects.all()
    fields = ['name', 'email']
    success_url = reverse_lazy('customers-list')

class CustomerDelete(DeleteView):
    queryset = Customer.tenant_objects.all()
    success_url = reverse_lazy('customers-list') 