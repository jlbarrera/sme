from django.conf.urls import patterns, include, url
from core.views.Employee import *

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
    url(r'^employees/$', EmployeeList.as_view()),
    url(r'^employees/add/$', EmployeeCreate.as_view(), name='employee_add'),
    url(r'^employees/(?P<pk>\d+)/$', EmployeeDetail.as_view(), name='employee_detail'),
    url(r'^employees/(?P<pk>\d+)/edit/$', EmployeeUpdate.as_view(), name='employee_update'),
    url(r'^employees/(?P<pk>\d+)/delete/$', EmployeeDelete.as_view(), name='employee_delete'),
    
    url(r'^login-failed/$', EmployeeDelete.as_view(), name='login-failed'),
    url(r'^account-disabled/$', EmployeeDelete.as_view(), name='account-disabled'),
    
    url(r'^login/$', 'core.views.auth.login_view', name='login'),
)
