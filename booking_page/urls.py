from django.urls import path
from . import views

urlpatterns = [
    path('',views.getWelcomePage),
    path('about/',views.getAboutPage),
    path('booking/',views.getBookingPage),
    path('success/',views.getSuccessPage)
]