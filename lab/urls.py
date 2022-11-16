from django.urls import path
from lab import views


urlpatterns = [
    path('',views.home,name="lab_home")
]