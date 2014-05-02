from django.db import models
from django.contrib.auth.models import User, Group
from multitenant.models import Tenant, TenantModel
from django.utils.translation import ugettext_lazy as _


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

class EmployeeManager(models.Manager):
    def create_employee(self, username, password):
        #Create the user
        user = User(username=username, password=password)
        user.save()
        #Assign default role
        Group.objects.filter(pk=id)
        #Create tenant
        tenant = Tenant(name=username)
        tenant.save()
        employee = self.create(name=username, user=user, tenant=tenant)        
        return employee
    
class Employee(Person):    
    role = models.OneToOneField(Group)
    paysheet = models.FloatField(blank=True, null=True)
    company_cost = models.FloatField(blank=True, null=True)    
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company, blank=True, null=True)
    
    objects = EmployeeManager()

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
    external = models.ForeignKey(External, blank=True, null=True)
    entity = models.ManyToManyField(Entity,null=True,blank=True)

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