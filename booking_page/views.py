from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.template import loader
from .forms import BookingForm

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
            return redirect('/')

        else:
            form=BookingForm(request.POST)
            template=loader.get_template('booking.html')
            context={
                'form':form
            }

            return HttpResponse(template.render(context,request))