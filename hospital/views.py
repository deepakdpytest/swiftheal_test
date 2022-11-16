from django.shortcuts import render,redirect 
from hospital.models import Hospital


def homi(request):
    if('hospital' in request.session):
        hospitaleldetails=Hospital.object.get(userID=request.session['hopital'])
        parameters={"name":hospitaldetails.name}
        return render(request,'profilePage.html',parameters)
    else:
        return redirect('home')
