from django.contrib import admin
from django.urls import path
from home import views





urlpatterns = [
    
    path("",views.index, name='index'),
    path("home",views.home, name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("services",views.services,name='services'),
    path("login",views.login,name='login')
    
    
]
