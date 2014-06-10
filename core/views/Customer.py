from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from core.models import Customer

class CustomerList(ListView):        
    paginate_by = 10
    
    def get_queryset(self):
        return Customer.tenant_objects.all().order_by('id').reverse() 

class CustomerDetail(DetailView):
    
    def get_queryset(self):
        return Customer.tenant_objects.all()
    
class CustomerCreate(CreateView):
    model = Customer
    fields = ['name', 'surname']
    success_url = reverse_lazy('customers-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CustomerCreate, self).form_valid(form)

class CustomerUpdate(UpdateView):    
    fields = ['name', 'surname']
    success_url = reverse_lazy('customers-list')
    
    def get_queryset(self):
        return Customer.tenant_objects.all()

class CustomerDelete(DeleteView):
    success_url = reverse_lazy('customers-list')
    
    def get_queryset(self): 
        Customer.tenant_objects.all()