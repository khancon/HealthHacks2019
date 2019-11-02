from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.utils import timezone
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
from .forms import PatientForm
from django.forms import modelformset_factory
import csv
from django.utils.encoding import smart_str

#Take data from django model Patient and export to csv file for processing in the Health Hacks pipeline
def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Title"),
        smart_str(u"Description"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.title),
            smart_str(obj.description),
        ])
    return response

#Show form for patient/doctors to input patient information daily that will be saved in the django model Patient
def index(request):
    if request.method == 'GET':
        form = PatientForm()
    elif request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient_name = form.cleaned_data.get('patient_name')
            age = form.cleaned_data.get('age')
            address = form.cleaned_data.get('address')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            zip_code = form.cleaned_data.get('zip_code')
            phone_number = form.cleaned_data.get('phone_number')
            illnesses = form.cleaned_data.get('illnesses')
            patient_description = form.cleaned_data.get('patient_description')
            stand_and_walk = form.cleaned_data.get('stand_and_walk')
            nausea = form.cleaned_data.get('nausea')
            pills_or_iv = form.cleaned_data.get('pills_or_iv')
            normal_breathing = form.cleaned_data.get('normal_breathing')
            normal_bp = form.cleaned_data.get('normal_bp')
            peebility = form.cleaned_data.get('peebility')
            bowels_movement_ok = form.cleaned_data.get('bowels_movement_ok')
        patient_obj = Patient(
            patient_name=patient_name, 
            age=age, 
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            phone_number=phone_number,
            illnesses=illnesses,
            patient_description=patient_description,
            stand_and_walk=stand_and_walk,
            nausea=nausea,
            pills_or_iv=pills_or_iv,
            normal_breathing=normal_breathing,
            normal_bp=normal_bp,
            peebility=peebility,
            bowels_movement_ok=bowels_movement_ok    
        )
        patient_obj.save()
    return render(request, 'survey/index.html', {
        'form': form,
        'heading': 'Daily Patient Form'
    })