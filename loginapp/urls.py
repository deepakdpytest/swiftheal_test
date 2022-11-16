from django.urls import path
from loginapp import views


urlpatterns = [
    path('pathologist',views.labr,name="login_lab"),
    path('doctor',views.dctr,name="login_doctor"),
    path('patient',views.patient,name="login_patient")
]
