from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from smecal.models import Event, EventForm
from core.models import Sale
from datetime import date 

class EventList(ListView):    
    
    paginate_by = 10

    def get_queryset(self):
        return Event.tenant_objects.all().order_by('when').reverse()

class EventToday(ListView):        
    
    paginate_by = 10
    
    def get_queryset(self):
        min_h = str(date.today())+' 00:00:00'    
        max_h = str(date.today())+' 23:59:59'
        return Event.tenant_objects.filter(when__gt=min_h, when__lt=max_h).order_by('when').reverse()    
    
class EventDetail(DetailView):    
    def get_queryset(self):
        return Event.tenant_objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)                
        sale = Sale.tenant_objects.filter(entity=self.object)
        if len(sale) > 0:
            context['sale'] = sale        
        return context
    
class EventCreate(FormView):
    form_class = EventForm
    template_name = 'smecal/event_form.html'    
    success_url = reverse_lazy('events-today')    
         
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.status = 'U'
        form.save()
        return super(EventCreate, self).form_valid(form)

class EventUpdate(UpdateView):    
    fields = ['when', 'duration', 'status', 'price', 'customer', 'employee']
    success_url=reverse_lazy('events-today')

    def get_queryset(self):
        return Event.tenant_objects.all()
    
class EventDelete(DeleteView):    
    success_url = reverse_lazy('events-today')

    def get_queryset(self):
        return Event.tenant_objects.all()

class EventPay(UpdateView):    
    fields = ['status']    
    template_name = 'smecal/event_pay.html'    

    def get_queryset(self):
        return Event.tenant_objects.all()
        
    def form_valid(self, form):  
        sale = Sale.tenant_objects.filter(entity=self.object)
        if not sale:      
            sale = Sale(customer=self.object.customer, 
                        tenant=self.object.tenant, 
                        amount=self.object.price,
                        customized_amount=False,
                        paid=False)
            sale.save()
            sale.entity.add(self.object)
            sale.save()
        else:
            sale = Sale.tenant_objects.filter(entity=self.object)[0]       
        return HttpResponseRedirect(reverse_lazy('sale-pay', args=[sale.id]))    