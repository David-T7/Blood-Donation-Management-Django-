from django.db import models
import uuid
from Donor.models import Donor

blood_type = [
    ( None, 'type'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+' , 'A+'),
    ('B+','B+'),
    ('AB+' ,'AB-')
    ]

class Blood(models.Model):
    Blood_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    Donor_id = models.ForeignKey(Donor , on_delete=models.DO_NOTHING, null=True , blank=True , unique=False)
    BloodGroup = models.CharField(max_length=20 ,  choices=blood_type)
    PackNo = models.CharField(max_length=20)
    RegDate = models.DateTimeField(auto_now_add=True)
    ExpDate = models.DateTimeField(max_length=10)
    QuantityOfBlood = models.CharField(max_length=4)
  
