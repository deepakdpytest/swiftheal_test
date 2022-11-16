from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("", views.index, name = 'home'),
    path("logout", views.logout, name = 'logout'),
    path("home", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("profile", views.profile, name = 'profile'),
    path("tips&facts", views.tips_facts, name = 'tips&facts'),
    path("appointments", views.appointments, name = 'appointments'),
    path("doctor", views.doctor, name = 'doctor'),
    path("calendar", views.calendar, name = 'calendar'),
    path("patientProfile", views.patientProfile, name = 'patientProfile'),
    path("symptom", views.symptom, name = 'sympyom')
]
