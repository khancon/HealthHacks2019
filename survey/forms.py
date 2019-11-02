from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.forms.models import inlineformset_factory
from .models import Patient

class PatientForm(forms.Form):
    patient_name = forms.CharField(
        label='Patient Name:',
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Patient Name'
        }),
        required=True)
    age = forms.IntegerField(
        label='Age:',
        widget=forms.TextInput(attrs={
            'placeholder': '999'
        }),
        required=True)
    address = forms.CharField(
        label='Address:',
        max_length=480,
        widget=forms.TextInput(attrs={
            'placeholder': 'Address'
        }),
        required=True)
    city = forms.CharField(
        label='City:',
        max_length=480,
        widget=forms.TextInput(attrs={
            'placeholder': 'City'
        }),
        required=True)
    state = forms.CharField(
        label='State:',
        max_length=480,
        widget=forms.TextInput(attrs={
            'placeholder': 'State'
        }),
        required=True)
    zip_code = forms.IntegerField(
        label='Age:',
        widget=forms.TextInput(attrs={
            'placeholder': '99999'
        }),
        required=True)
    phone_number = forms.IntegerField(
        label="Phone Number",
        widget=forms.TextInput(attrs={
            'placeholder': '9999999999'
        }),
        required=True)
    state = forms.CharField(
        label='State:',
        max_length=480,
        widget=forms.TextInput(attrs={
            'placeholder': 'State'
        }),
        required=True)
    illnesses = forms.CharField(
        label='Ilness:',
        max_length=1000,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ilness'
        }),
        required=True)
    patient_description = forms.CharField(
        label='Patient Description:',
        max_length=1000000,
        widget=forms.TextInput(attrs={
            'placeholder': 'Patient Description'
        }),
        required=True)
    stand_and_walk = forms.CharField(
        label='Can you Stand and Walk?',
        max_length=1000000,
        widget=forms.TextInput(attrs={
            'placeholder': 'Yes or No'
        }),
        required=True)
    nausea = forms.CharField(
        label='Do you expeience nausea under control?',
        max_length=1000000,
        widget=forms.TextInput(attrs={
            'placeholder': 'Yes or No'
        }),
        required=True)
    pills_or_iv = forms.CharField(
        label='Is your pain eased through pills or medicine delivered through your IV?',
        max_length=1000000,
        widget=forms.TextInput(attrs={
            'placeholder': 'Pills or IV'
        }),
        required=True)
    normal_breathing = forms.CharField(
        label='Breath rate?',
        max_length=1000000,
        widget=forms.TextInput(attrs={
            'placeholder': ''
        }),
        required=True)
    normal_bp = forms.CharField(
        label='Blood Pressure',
        max_length=1000000,
        widget=forms.TextInput(attrs={
            'placeholder': 'ex: 120 b/m'
        }),
        required=True)
    peebility = forms.CharField(
        label='Can you pee normally?',
        max_length=1000000,
        widget=forms.TextInput(attrs={
            'placeholder': 'Yes or No'
        }),
        required=True)
    bowels_movement_ok = forms.CharField(
        label='Do you normal bowel movement?',
        max_length=1000000,
        widget=forms.TextInput(attrs={
            'placeholder': 'Yes or No'
        }),
        required=True)






