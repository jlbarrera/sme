from django.db import models
from django import forms
from core.models import Entity, Customer, Employee, EntityForm
from django.utils.translation import ugettext_lazy as _

STATUS = (
        ('P', _("Paid")),
        ('U', _("Unpaid")),                
        ('C', _("Canceled")),        
    )

class Event(Entity):
    when = models.DateTimeField()
    duration = models.TimeField()
    status = models.CharField(max_length=200, blank=True, choices=STATUS)
    customer = models.ForeignKey(Customer)
    employee = models.ForeignKey(Employee, blank=True, null=True)

class EventForm(EntityForm):
    class Meta:
        model = Event
        exclude = ['tenant', 'name', 'status']
        
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
    
    when = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder':_('Enter DateTime')}))
    duration = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder':_('Enter Duration')}))  