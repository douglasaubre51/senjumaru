from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.template import loader
from .forms import BookingForm
from .models import Booking
from .choices import RoomChoices

# Create your views here.
def getWelcomePage(request):
    return render(request,'welcome.html')

def getAboutPage(request):
    return render(request,'about.html')

def getBookingPage(request):
    if(request.method=='GET'):
        form=BookingForm
        template=loader.get_template('booking.html')
        context={
            'form':form
        }

        return HttpResponse(template.render(context,request))

    elif(request.method=="POST"):
        form=BookingForm(request.POST)

        if(form.is_valid()):
            form.save()
            return getSuccessPage(request,form)

        else:
            form=BookingForm(request.POST)
            template=loader.get_template('booking.html')
            context={
                'form':form
            }

            return HttpResponse(template.render(context,request))

def getSuccessPage(request,form):
    email=form.cleaned_data['email']
    template=loader.get_template('success.html')
    booked=Booking.objects.get(email=email)
    room=''

    for i in RoomChoices:
        if i==booked.room_types:
            room=i.name

    context={
        'booked':booked,
        'room':room
    }

    return HttpResponse(template.render(context,request))