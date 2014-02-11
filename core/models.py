from django.db import models
from django.contrib.auth.models import User
from multitenant.models import TenantModel

class Person(TenantModel):
    passport = models.CharField(max_length=200)
    name = models.CharField(max_length=200)    
    surname = models.CharField(max_length=200)
    mobile = models.IntegerField()
    telephone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    born = models.DateField()
    
    class Meta:
        abstract = True

class Employee(Person):
    user = models.OneToOneField(User)
    type = models.CharField(max_length=200)
    paysheet = models.FloatField()
    company_cost = models.FloatField()

class Customer(Person):
    notes = models.CharField(max_length=8000)

class External(Person):
    assigment = models.FloatField()
    
class CashFlow(TenantModel):
    amount = models.IntegerField()
    datetime = models.DateTimeField()
    type = models.CharField(max_length=200)
    paymentform = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    customized_amount = models.BooleanField()
    paid = models.BooleanField()
 
class Discount(TenantModel):
    percentage = models.IntegerField()

class Number(TenantModel):
    number = models.IntegerField()

class Sale(CashFlow):        
    discount = models.OneToOneField (Discount)
    number = models.OneToOneField (Number)
       
class Outlay(CashFlow):
    dateofpaid = models.DateField()
    
class Entity(TenantModel):
    name = models.CharField(max_length=200)
    
    class Meta:
        abstract = True

class Company(TenantModel):
    name = models.CharField(max_length=200)

class Categoty(TenantModel):
    name = models.CharField(max_length=200)