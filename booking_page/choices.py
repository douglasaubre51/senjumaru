from django.db import models
from django.utils.translation import gettext_lazy as _

class RoomChoices(models.IntegerChoices):
    DELUXE=1,_('Deluxe')
    EXECUTIVE=2,_('Executive')
    JUNIOR=3,_('Junior Suite')
    FULLSUITE=4,_('Full Suite')
    PRESIDENTIALSUITE=5,_('Presidential Suite')
    PENTHOUSESUITE=6,_('Penthouse Suite')
    OVERWATERBUNGALOW=7,_('Overwater Bungalow')
    VILLA=8,_('Villa')