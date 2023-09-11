from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
import datetime as dt

class ProfileForm(forms.Form):
    addressLine1=forms.CharField(
        required=True,
        label='Address Line 1',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Address Line 1'}),)
    

addressLine2=forms.CharField(
        required=False,
        label='Address Line 2',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Address Line 2'}),)

city=forms.CharField(
        required=True,
        label='City',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter City'}),)

province= forms.CharField(
        required=True,
        label='Province',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Province'}),)

country=forms.CharField(
        required=True,
        label='Country',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Country'}),)

postalCode=forms.CharField(
        required=True,
        label='Postal Code',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Postal Code'}),)



def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Row(Column('addressLine1', css_class='form-group col-md-6'),Column('addressLine1' ,css_class="form-group col-md-6")),
        Row(Column('city', css_class='form-group col-md-6'),Column('province' ,css_class="form-group col-md-6")),
        Row(Column('country', css_class='form-group col-md-6'),Column('postalCode' ,css_class="form-group col-md-6")),
        Submit('submit', 'Save Changes', css_class='btn btn-primary me-2')
            
            )
    
        
        





class Meta:
    model = Profile
    fields=['addressLine1', 'addressLine2', 'city', 'province', 'country', 'postal code']