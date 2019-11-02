from django.contrib import admin

from .models import Patient, SurveyResponses

# Register your models here.
admin.site.register(Patient)
admin.site.register(SurveyResponses)
