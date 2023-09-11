from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
import datetime as dt

class ProfileForm(forms.Form):
    addressLine1=forms.CharField(
        required=True,
        label='Address Line 1',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address Line 1'}),)
    

addressLine2=forms.CharField(
        required=False,
        label='Address Line 2',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address Line 2'}),)

city=forms.CharField(
        required=True,
        label='City',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),)

province= forms.CharField(
        required=True,
        label='Province',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Province'}),)

country=forms.CharField(
        required=True,
        label='Country',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Country'}),)

postalCode=forms.CharField(
        required=True,
        label='Postal Code',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Postal Code'}),)