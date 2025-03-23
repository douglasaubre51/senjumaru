from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking

        fields=['username','email','phone_no','room_types','chosen_date']
        # to get the date picker
        widgets={
            'chosen_date':forms.DateInput(attrs={'type':'date'})
        }