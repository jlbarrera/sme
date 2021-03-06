from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from core.models import Sale
from datetime import date 

class SaleList(ListView): 
       
    paginate_by = 10

    def get_queryset(self):
        return Sale.tenant_objects.all().order_by('datetime').reverse()

    def get_context_data(self, **kwargs):
        context = super(SaleList, self).get_context_data(**kwargs)                
        totalday = 0        
        for sale in self.get_queryset():
            totalday += sale.amount 
        context['total'] = totalday        
        return context

class SaleToday(ListView):        
    
    paginate_by = 10
    
    def get_queryset(self):
        min_h = str(date.today())+' 00:00:00'    
        max_h = str(date.today())+' 23:59:59'
        return Sale.tenant_objects.filter(datetime__gt=min_h, datetime__lt=max_h).order_by('datetime').reverse()
    
    def get_context_data(self, **kwargs):
        context = super(SaleToday, self).get_context_data(**kwargs)                
        totalday = 0        
        for sale in self.get_queryset():
            totalday += sale.amount 
        context['total'] = totalday        
        return context

class SaleDetail(DetailView):
    
    def get_queryset(self):    
        return Sale.tenant_objects.all()
    
class SaleCreate(CreateView):
    model = Sale
    fields = ['customer', 'amount', 'customized_amount', 'paid', 'entity']
    success_url = reverse_lazy('sales-today')
    
    def form_valid(self, form):
        form.instance.user = self.request.user        
        return super(SaleCreate, self).form_valid(form)

class SaleUpdate(UpdateView):
    queryset = Sale.tenant_objects.all()
    fields = ['customer', 'amount', 'customized_amount', 'paid', 'entity']
    success_url=reverse_lazy('sales-today')

class SaleDelete(DeleteView):
    success_url = reverse_lazy('sales-today')
    
    def get_queryset(self):    
        return Sale.tenant_objects.all()

class SalePay(UpdateView):    
    fields = ['paid']    
    template_name = 'core/sale_pay.html'
    success_url = reverse_lazy('sales-today')
    
    def get_queryset(self):    
        return Sale.tenant_objects.all()
    
    def form_valid(self, form):
        if form.instance.paid:
            for entity in self.object.entity.all():
                if hasattr(entity, 'event'):
                    entity.event.status = 'P'
                    entity.event.save()
        return super(SalePay, self).form_valid(form)
    