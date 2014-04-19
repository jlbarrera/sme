from django.forms import ModelForm
from core.models import *

class BaseForm(ModelForm):
    error_css_class = 'has-error'
    required_css_class = 'required'
    
class AuthorForm(BaseForm):
    class Meta:
        model = Employee

class CustomerForm(BaseForm):
    class Meta:
        model = Customer

class SaleForm(BaseForm):
    class Meta:
        model = Sale