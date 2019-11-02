from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.forms.models import inlineformset_factory
from .models import Patient, SurveyResponses

