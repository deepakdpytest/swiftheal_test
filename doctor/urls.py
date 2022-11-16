from django.urls import path
from doctor import views


urlpatterns = [
    path('dr',views.homes,name="doctor_home")
]