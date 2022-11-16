from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from analyzer.models import Symptom
from patient.models import Patient
from datetime import date
from analyzer.analyser import twoWayMapper, changeform, strtoarr,arrtostr, symptomanalyser, predict
import json
# Create your views here.
def analyser(request):
    if('patient' in request.session):
        return render(request,'analyser.html')
    return redirect('home')

@api_view(['GET','POST'])
def symptom(request):
    if(request.method=='POST'):
        params=request.data
        try:
            if(params['start']=='start'):
                #initiliaze the analyser to deliver messages.
                patientdetails = Patient.objects.get(Patient_AdharId=request.session['patient'])
                name=patientdetails.Name
                symp=Symptom(user=request.session['patient'],time=date.today())
                symp.save()
                params={"question": f"Heyy!!! {name}. I am a symptom analyser. Now, please answer my questions correctly to help me to diagnose you properly\nThankyou","type": "message"}
                return JsonResponse(params,safe=False)
        except:
            # try:
                # if status is selected asking category 
                symp=Symptom.objects.filter(user=request.session['patient']).last()
                if(symp.status=='started'):
                    categories=[]
                    with open('data.json','r') as f:
                        categories=json.load(f)
                        categories=categories['categories']
                    params={"question":"Please select the appropriate category in which your major symptom lies.","type":"select","options":categories,"multiple":False}
                    symp.status='selected'
                    symp.save()
                    return JsonResponse(params,safe=False)
                
                elif(symp.status=='selected'):
                    #if status is selected then give subcategory questions
                    res=params['response']
                    subcategories=None
                    with open('data.json','r') as f:
                        subcategories=json.load(f)
                        subcategories=subcategories['symptoms']
                    params={"question":"Please select all the symptoms which apply to you.","type":"select","options":subcategories[res[0]],"multiple":True}
                    symp.status='active'
                    symp.save()
                    return JsonResponse(params,safe=False)
                
                elif(symp.status=='active'):
                    res=request.data['response']
                    res=changeform(res,' ')
                    rep=strtoarr(symp.symps)
                    flag=strtoarr(symp.flag)
                    rp=symptomanalyser(res,rep,flag)
                    ques=rp['question']
                    rep=arrtostr(rp['rep'])
                    flag=arrtostr(rp['flag'])
                    symp.symps=rep
                    symp.flag=flag
                    symp.status=rp['status']
                    symp.save()
                    if(len(ques)==0):
                        params={"question":"Your diagnosis had been completed","type":"message"}
                        return JsonResponse(params)
                    ques=changeform(ques,'_')
                    ques.append('None of these')
                    params={"question":"Please select the symptoms which you are feeling","type":"select","options":ques,"multiple":True}
                    return JsonResponse(params)
                
                elif(symp.status=='diagnosed'):
                    rep=symp.symps
                    a=predict(strtoarr(rep))
                    if(len(a)==0):
                        symp.status='unsucessfull'
                        symp.save()
                        params={"question":"We are unable to predict your disease.\nHowever, we would send your diagnosis report to a professinal doctor for further investigation.","type":"message"}
                        return JsonResponse(params)
                    symptoms=""
                    for i in range(len(a)-1):
                        symptoms+=a[i]+", "
                    symptoms+=a[len(a)-1]
                    params={"question":f"following could be the possibilities of your diseases: \n{symptoms}\nWe would send your diagnostic report to a professional doctor for confirmation","type":"message"}
                    symp.predicted=symptoms
                    symp.status='sucessfull'
                    symp.save()
                    return JsonResponse(params)
                
                elif(symp.status=='sucessfull' or symp.status=='unsucessfull'):
                    params={"type":"end"}
                    return JsonResponse(params)
                
                else:
                    return HttpResponse(404)

        return JsonResponse(params)
    else:
        return redirect('home')
