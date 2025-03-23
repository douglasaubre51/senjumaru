from django.shortcuts import redirect,render

# Create your views here.
def getWelcomePage(request):
    return render(request,'welcome.html')

def getAboutPage(request):
    return render(request,'about.html')
