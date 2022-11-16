from django.shortcuts import render,redirect
from doctor.models import Doctor
from hospital.models import Hospital
def homes(request):
    if('doctor' in request.session):
        doctordetails=Doctor.objects.get(Doctor_id=request.session['doctor'])
        parameters={"UserId":doctordetails.Doctor_id,"status":"Doctor","name":doctordetails.Name,"age":doctordetails.Age,"aadhar_id":doctordetails.Aadhar_id,"phone_number":doctordetails.Mobile_no,"email":doctordetails.Email}
        hospital=Hospital.objects.get(Hospital_id=doctordetails.Hospital_id)
        parameters['hospital']=hospital.Name_hs
        if(doctordetails.Gender=='F'):
            parameters['gender']='Female'
        elif(doctordetails.Gender=='M'):
            parameters['gender']='Male'
        else:
            parameters['gender']='Other'
        return render(request,'profilePage.html',parameters)
    else:
        return redirect('home')

