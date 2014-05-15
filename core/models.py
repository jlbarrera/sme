from django.db import models
from django import forms
from django.contrib.auth.models import User, Group
from multitenant.models import TenantModel
from django.utils.translation import ugettext_lazy as _
from multitenant.forms import TenantModelForm

GENDER = (
        ('M', _("Male")),        
        ('F', _("Female"))
    )

class Person(TenantModel):
    name = models.CharField(max_length=200, unique = True)
    passport = models.CharField(max_length=200, null=True, blank=True)        
    surname = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.IntegerField(blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    province = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True, choices=GENDER)
    born = models.DateField(blank=True, null=True)
    
    class Meta:
        abstract = True

class Company(TenantModel):
    name = models.CharField(max_length=200)    
    code = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    postal_code = models.IntegerField(blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
  
class Employee(Person):    
    role = models.ManyToManyField(Group, blank=True, null=True)    
    paysheet = models.FloatField(blank=True, null=True)
    company_cost = models.FloatField(blank=True, null=True)    
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company, blank=True, null=True)
    
class Customer(Person):
    notes = models.CharField(max_length=8000, null=True, blank=True)
    
    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)

class External(Person):
    assigment = models.FloatField()

class Entity(TenantModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

class EntityForm(TenantModelForm):
    class Meta:
        model = Entity
        exclude = ['tenant']
        
    def __init__(self, *args, **kwargs):
        super(EntityForm, self).__init__(*args, **kwargs)
    
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':_('Enter Description')}))  
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':_('Enter Price')}))
    
class CashFlow(TenantModel):
    amount = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=200)
    paymentform = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    customized_amount = models.BooleanField()
    paid = models.BooleanField()    

class Sale(CashFlow):        
    customer = models.ForeignKey(Customer)
    external = models.ForeignKey(External, blank=True, null=True)
    entity = models.ManyToManyField(Entity,null=True,blank=True)
    
    def __unicode__(self):
        return '%s' % (self.amount)

class Discount(TenantModel):
    percentage = models.IntegerField()
    sale = models.ForeignKey(Sale)
        
class Number(TenantModel):
    number = models.IntegerField()
    sale = models.ForeignKey(Sale)        
      
class Outlay(CashFlow):
    dateofpaid = models.DateField(blank=True)
    
class Category(TenantModel):
    name = models.CharField(max_length=200)