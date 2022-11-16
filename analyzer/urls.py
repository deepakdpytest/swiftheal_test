from django.urls import path
from analyzer import views

urlpatterns=[
    path('',views.analyser,name='analyser'),
    path('symptom',views.symptom,name='symptom')
]