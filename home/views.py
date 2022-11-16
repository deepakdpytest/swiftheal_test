from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if('doctor' in request.session):
        paramaters={'profileLink':'/doctor/dr'}
    elif('patient' in request.session):
        paramaters={'profileLink':'/patient/p'}
    else:
        paramaters={'profileLink':'#'}
    return render(request, 'index.html',paramaters)

def logout(request):
    parameters={'profileLink':'#'}
    if('patient' in request.session):
        del request.session['patient']
    elif('doctor' in request.session):
        del request.session['doctor']
    elif('lab' in request.session):
        del request.session['lab']
    else:
        return redirect('home')
    return redirect('home')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profilePage.html')

def tips_facts(request):
    return render(request, 'tips&facts.html')

def appointments(request):
    return render(request, 'appointments.html')

def doctor(request):
    return render(request, 'doctor.html')

def calendar(request):
    return render(request, 'calendar.html')

def patientProfile(request):
    return render(request, 'patientProfile.html')

def symptom(request):
    return render(request, 'symptom.html')