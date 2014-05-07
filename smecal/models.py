from django.db import models
from core.models import Entity, Customer, Employee
from django.utils.translation import ugettext_lazy as _
from multitenant.forms import TenantModelForm

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

class EventForm(TenantModelForm):
    class Meta:
        model = Event
        exclude = ['tenant', 'name']
        
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)  