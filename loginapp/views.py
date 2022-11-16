from django.shortcuts import render,redirect
from lab.models import Lab
from doctor.models import Doctor
from patient.models import Patient

def labr(request):
    if('lab' in request.session):
        return redirect('lab_home')
    else:
        if(request.method=='POST'):
            userID=request.POST['UserID']
            password=request.POST['password']
            try:
                labdetails=Lab.objects.get(Lab_id=userID)
                if(labdetails.Password==password):
                    request.session['lab']=userID
                    return redirect('lab_home')
            except Exception as e:
                return redirect('home')
    return redirect('home')

def dctr(request):
    if('doctor' in request.session):
        return redirect('doctor_home')

    else:
        if(request.method=='POST'):
            userID=request.POST['UserID']
            password=request.POST['password']
            try:
                doctordetails=Doctor.objects.get(Doctor_id=userID)
                if(doctordetails.Password==password):
                    request.session['doctor']=userID
                    return redirect('doctor_home')
            except Exception as e:
                return redirect('home')
    return redirect('home')



def patient(request):
    if('patient' in request.session):
        return redirect('patient_home')

    else:
        if(request.method=='POST'):
            userID=request.POST['UserID']
            password=request.POST['password']
            try:
                patientdetails=Patient.objects.get(Patient_AdharId=userID)
                if(patientdetails.Password==password):
                    request.session['patient']=userID
                    return redirect('patient_home')
            except Exception as e:
                return redirect('home')
    return redirect('home')



