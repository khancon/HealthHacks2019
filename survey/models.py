from django.db import models
import uuid
import datetime


# Create your models here.
#class Patient(models.Model):
    #patient-
    
class Patient(models.Model):
    '''
    Patient ID
    Doctor ID (head doctor)
    Nurse ID (attending nurse)
    Name 
    Age 
    Illness 
    Address
    Phone number
    Emergency contact ID
    Are able to stand and walk
Have any nausea under control
Can ease your pain with pills instead of medicine you get through an IV
Have normal breathing and blood pressure
Think and respond as well as you did before the surgery
Are able to pee and have a bowel movement

    '''

    #patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_name = models.CharField(max_length=200, default="Name")
    timestamp = models.DateTimeField(default=datetime.datetime.now, blank=True)
    age = models.IntegerField(default= 999)
    address = models.CharField(max_length=480, default='Address')
    city = models.CharField(max_length=480, default='City')
    state = models.CharField(max_length=2, default="XX")
    zip_code = models.IntegerField(default=99999)
    phone_number = models.IntegerField(default=9999999999)
    illnesses = models.CharField(max_length=1000, default="Illness")
    patient_description = models.CharField(max_length=1000000, default="Illness")
    stand_and_walk = models.CharField(max_length=1000, default="Yes or No")
    nausea = models.CharField(max_length=1000, default="Yes or No")
    pills_or_iv = models.CharField(max_length=1000, default="Pills or IV")
    normal_breathing = models.CharField(max_length=1000, default="Yes or No")
    normal_bp = models.CharField(max_length=1000, default="Yes or No")
    peebility = models.CharField(max_length=1000, default="Yes or No")
    bowel_movement_ok = models.CharField(max_length=1000, default="Desc.")
    
