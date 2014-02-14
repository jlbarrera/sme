from django.db import models
from django.contrib.auth.models import User
from multitenant.models import TenantModel

class Person(TenantModel):
    name = models.CharField(max_length=200)
    passport = models.CharField(max_length=200, blank=True)        
    surname = models.CharField(max_length=200, blank=True)
    mobile = models.IntegerField(blank=True)
    telephone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    postal_code = models.IntegerField(blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    born = models.DateField(blank=True)
    
    class Meta:
        abstract = True

class Company(TenantModel):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    postal_code = models.IntegerField(blank=True)
    telephone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)

class Employee(Person):    
    type = models.CharField(max_length=200)
    paysheet = models.FloatField(blank=True)
    company_cost = models.FloatField(blank=True)    
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company)

class Customer(Person):
    notes = models.CharField(max_length=8000, blank=True)

class External(Person):
    assigment = models.FloatField()

class Entity(TenantModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    price = models.IntegerField()
    created = models.DateTimeField()
    
class CashFlow(TenantModel):
    amount = models.IntegerField()
    datetime = models.DateTimeField()
    type = models.CharField(max_length=200)
    paymentform = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    customized_amount = models.BooleanField()
    paid = models.BooleanField()

class Sale(CashFlow):        
    customer = models.ForeignKey(Customer)
    external = models.ForeignKey(External, blank=True)

class Discount(TenantModel):
    percentage = models.IntegerField()
    sale = models.ForeignKey(Sale)
    entity = models.ForeignKey(Entity)    

class Number(TenantModel):
    number = models.IntegerField()
    sale = models.ForeignKey(Sale)    
    entity = models.ForeignKey(Entity)
      
class Outlay(CashFlow):
    dateofpaid = models.DateField(blank=True)
    
class Category(TenantModel):
    name = models.CharField(max_length=200)