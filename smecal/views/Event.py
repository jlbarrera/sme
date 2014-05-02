from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from smecal.models import Event 

class EventList(ListView):    
    queryset = Event.tenant_objects.all()

class EventDetail(DetailView):
    queryset = Event.tenant_objects.all()
    
class EventCreate(CreateView):
    model = Event
    fields = ['when', 'duration', 'status', 'price', 'created']
    success_url = reverse_lazy('events-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate, self).form_valid(form)

class EventUpdate(UpdateView):
    queryset = Event.tenant_objects.all()
    fields = ['when', 'duration', 'status', 'price', 'created']
    success_url=reverse_lazy('events-list')

class EventDelete(DeleteView):
    queryset = Event.tenant_objects.all()
    success_url = reverse_lazy('events-list')