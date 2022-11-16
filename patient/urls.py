from django.urls import path
from patient import views


urlpatterns = [
    path('p',views.home,name="patient_home"),
    path('signup',views.signup,name="patient_signup"),
    path('appointments',views.appointment,name='patient_appointment'),
    path('book/<str:doctor_id>',views.book,name='book')
]