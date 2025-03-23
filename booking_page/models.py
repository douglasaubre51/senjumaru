from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from .choices import RoomChoices
# Create your models here.
class Booking(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone_no=models.IntegerField()
    room_types=models.IntegerField(choices=RoomChoices.choices, default=RoomChoices.DELUXE)
    chosen_date=models.DateField(default=date.today)