from django.urls import path
from . import views

urlpatterns = [
    path('',views.getWelcomePage),
    path('about/',views.getAboutPage)
]