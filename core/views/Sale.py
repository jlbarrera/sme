from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from core.models import Sale
from datetime import date, datetime 

class SaleList(ListView): 
       
    paginate_by = 10
    queryset = Sale.tenant_objects.all().order_by('datetime').reverse()

class SaleToday(ListView):        
    
    paginate_by = 10
    
    def get_queryset(self):
        min = str(date.today())+' 00:00:00'    
        max = str(date.today())+' 23:59:59'
        return Sale.tenant_objects.filter(datetime__gt=min, datetime__lt=max).order_by('datetime').reverse()
    
    def get_context_data(self, **kwargs):
        context = super(SaleToday, self).get_context_data(**kwargs)                
        totalday = 0        
        for sale in self.get_queryset():
            totalday += sale.amount 
        context['total'] = totalday        
        return context

class SaleDetail(DetailView):
    queryset = Sale.tenant_objects.all()    
    
class SaleCreate(CreateView):
    model = Sale
    fields = ['customer', 'amount', 'customized_amount', 'paid']
    success_url = reverse_lazy('sales-today')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.datetime = datetime.now()
        return super(SaleCreate, self).form_valid(form)

class SaleUpdate(UpdateView):
    queryset = Sale.tenant_objects.all()
    fields = ['customer', 'amount', 'customized_amount', 'paid']
    success_url=reverse_lazy('sales-today')

class SaleDelete(DeleteView):
    queryset = Sale.tenant_objects.all()
    success_url = reverse_lazy('sales-today')

class SalePay(UpdateView):
    queryset = Sale.tenant_objects.all()
    fields = ['paid']    
    template_name = 'core/sale_pay.html'
    success_url = reverse_lazy('sales-today')
    