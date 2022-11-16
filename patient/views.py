from django.shortcuts import render,redirect
from patient.models import Patient, Appointment
from doctor.models import Doctor
from hospital.models import Hospital
def home(request):
    if('patient' in request.session):
        patientdetails=Patient.objects.get(Patient_AdharId=request.session['patient'])
        parameters={"UserId":patientdetails.Patient_AdharId,"name":patientdetails.Name,"age":patientdetails.Age,"aadhar_id":patientdetails.Patient_AdharId,"phone_number":patientdetails.Mobile_no,"state":patientdetails.State,"address":patientdetails.Address,"pin":patientdetails.Pincode,"status":"Patient","email":patientdetails.email}
        if(patientdetails.Gender=='M'):
            parameters['gender']='Male'
        elif(patientdetails.Gender=='F'):
            parameters['gender']='Female'
        else:
            parameters['gender']='Others'
        
        return render(request,'patientProfile.html',parameters)
    else:
        return redirect('home')

def signup(request):
    if(request.method=='POST'):
        AadharId=request.POST['aadharID']
        Phone=request.POST['phone']
        Name=request.POST['name']
        Age=request.POST['age']
        Gender=request.POST['gender']
        State=request.POST['state']
        Address=request.POST['address']
        Pin=request.POST['pin']
        Password=request.POST['password']
        email=request.POST['email']
        try:
            patientdetails=Patient(Patient_AdharId=AadharId,Mobile_no=Phone,Name=Name,Age=Age,Gender=Gender,State=State,Address=Address,Pincode=Pin,Password=Password,email=email)
            patientdetails.save()
            request.session['patient']=AadharId
            return redirect('patient_home')
        except Exception as e:
            return redirect('home')
    return redirect('home')



def appointment(request):
    doctorlist=Doctor.objects.filter().all()
    doctorlist=list(doctorlist)
    for doctor in doctorlist:
        hospital=Hospital.objects.filter(Hospital_id=doctor.Hospital_id).first()
        doctor.hs_name=hospital.Name_hs
    parameters={'doctors':doctorlist}
    print(parameters)
    return render(request, 'doctor.html',parameters)

def book(request,doctor_id):
    if(request.method=='GET'):
        doctor=Doctor.objects.get(Doctor_id=doctor_id)
        parameters={"doctor":doctor}
        return render(request,'calender.html',parameters)
    if(request.method=='POST'):
        doctor_id=request.POST['doctor_id']
        dt=request.POST['dt']
        tme=request.POST['time']
        apt=Appointment(Patient_AdharId=request.session['patient'],Doctor_id=doctor_id,Appointment_date=dt,Appointment_time=tme)
        apt.save()
        return redirect('home')


