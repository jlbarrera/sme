from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from smecal.models import Event
from datetime import date 

class EventList(ListView):    
    
    paginate_by = 10

    def get_queryset(self):
        return Event.tenant_objects.all().order_by('when')

class EventToday(ListView):        
    
    paginate_by = 10
    
    def get_queryset(self):
        min_h = str(date.today())+' 00:00:00'    
        max_h = str(date.today())+' 23:59:59'
        return Event.tenant_objects.filter(when__gt=min_h, when__lt=max_h).order_by('when')    
    
class EventDetail(DetailView):
    queryset = Event.tenant_objects.all()
    
class EventCreate(CreateView):
    model = Event
    fields = ['when', 'duration', 'status', 'price', 'customer', 'employee']
    success_url = reverse_lazy('events-today')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate, self).form_valid(form)

class EventUpdate(UpdateView):
    queryset = Event.tenant_objects.all()
    fields = ['when', 'duration', 'status', 'price', 'created', 'customer', 'employee']
    success_url=reverse_lazy('events-today')

class EventDelete(DeleteView):
    queryset = Event.tenant_objects.all()
    success_url = reverse_lazy('events-today')