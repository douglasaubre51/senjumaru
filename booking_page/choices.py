from django.db import models
from django.utils.translation import gettext_lazy as _

class RoomChoices(models.IntegerChoices):
    DELUXE=1,_('Deluxe')
    EXECUTIVE=2,_('Executive')
    JUNIOR=3,_('Junior Suite')
    FULL=4,_('Full Suite')
    PRESIDENTIAL=5,_('Presidential Suite')
    PENTHOUSE=6,_('Penthouse Suite')
    OVERWATER=7,_('Overwater Bungalow')
    VILLA=8,_('Villa')