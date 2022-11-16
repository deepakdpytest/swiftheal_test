from django.shortcuts import render,redirect
from lab.models import Lab

def home(request):
    if('lab' in request.session):
        labdetails=Lab.objects.get(Lab_id=request.session['lab'])
        parameters={"name":labdetails.Lab_name}
        return render(request,'profilePage.html',parameters)
    else:
        return redirect('home')

# Create your views here.

