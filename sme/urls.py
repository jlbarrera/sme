from django.conf.urls import patterns, include, url
from core.views.Employee import EmployeeCreate, EmployeeDelete, EmployeeDetail, EmployeeList, EmployeeUpdate
from core.views.Customer import CustomerCreate, CustomerDelete, CustomerDetail, CustomerList, CustomerUpdate
from core.views.Sale import SaleCreate, SaleDelete, SaleDetail, SaleList, SaleUpdate, SaleToday, SalePay
from smecal.views.Event import EventCreate, EventDelete, EventDetail, EventList, EventUpdate, EventToday

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sme.views.home', name='home'),
    # url(r'^sme/', include('sme.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^login/$', 'core.views.auth.login_view', name='login'),
    url(r'^logout/$', 'core.views.auth.logout_view', name='logout'),
    url(r'^create-user/$', 'core.views.auth.createUser_view', name='create-user'),
    url(r'^login-failed/$', EmployeeDelete.as_view(), name='login-failed'),
    url(r'^account-disabled/$', EmployeeDelete.as_view(), name='account-disabled'),
    
    url(r'^$', 'core.views.base.index', name='index'),
    
    url(r'^employees/$', EmployeeList.as_view(), name='employees-list'),
    url(r'^employees/add/$', EmployeeCreate.as_view(), name='employee-add'),
    url(r'^employees/(?P<pk>\d+)/$', EmployeeDetail.as_view(), name='employee-detail'),
    url(r'^employees/(?P<pk>\d+)/edit/$', EmployeeUpdate.as_view(), name='employee-update'),
    url(r'^employees/(?P<pk>\d+)/delete/$', EmployeeDelete.as_view(), name='employee-delete'),
    
    url(r'^customers/$', CustomerList.as_view(), name='customers-list'),
    url(r'^customers/add/$', CustomerCreate.as_view(), name='customer-add'),
    url(r'^customers/(?P<pk>\d+)/$', CustomerDetail.as_view(), name='customer-detail'),
    url(r'^customers/(?P<pk>\d+)/edit/$', CustomerUpdate.as_view(), name='customer-update'),
    url(r'^customers/(?P<pk>\d+)/delete/$', CustomerDelete.as_view(), name='customer-delete'),
    
    url(r'^sales/$', SaleList.as_view(), name='sales-list'),
    url(r'^sales/today$', SaleToday.as_view(), name='sales-today'),
    url(r'^sales/add/$', SaleCreate.as_view(), name='sale-add'),
    url(r'^sales/(?P<pk>\d+)/$', SaleDetail.as_view(), name='sale-detail'),
    url(r'^sales/(?P<pk>\d+)/edit/$', SaleUpdate.as_view(), name='sale-update'),
    url(r'^sales/(?P<pk>\d+)/delete/$', SaleDelete.as_view(), name='sale-delete'),    
    url(r'^sales/(?P<pk>\d+)/pay/$', SalePay.as_view(), name='sale-pay'), 
    
    url(r'^events/$', EventList.as_view(), name='events-list'),
    url(r'^events/today$', EventToday.as_view(), name='events-today'),
    url(r'^events/add/$', EventCreate.as_view(), name='event-add'),
    url(r'^events/(?P<pk>\d+)/$', EventDetail.as_view(), name='event-detail'),
    url(r'^events/(?P<pk>\d+)/edit/$', EventUpdate.as_view(), name='event-update'),
    url(r'^events/(?P<pk>\d+)/delete/$', EventDelete.as_view(), name='event-delete'),   
)
