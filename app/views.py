from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Department, Patient, Doctor
from .forms import DoctorForm
import json
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.

def index(request):
    doctor_name = Doctor.objects.get(pk=1)
    dep_name = Department.objects.get(pk=1)

    depart = Department.objects.filter().all()
    patient = Patient.objects.filter().all()
    doctor = Doctor.objects.filter().all()
    request1 = Patient.objects.filter(doctor=1).values('name', 'department__title')
    info = {'depart': depart,
            'patient': patient,
            'doctor': doctor,
            'request1': request1}
    a = render(request, "index.html", info)
    #re = JsonResponse({'doctor': list(request1)})
    #print(re.content)

    return a

def request_pacient_of_doc(request):

    if request.method == "POST":
        id = request.POST['id_doc']
    doc = Doctor.objects.filter(id=id).values('name')
    req1 = Patient.objects.filter(doctor=id).values('name', 'department__title')
    info = {'request1': req1,
            'doc': doc}
    a = render(request, "request1.html", info)
    return a

def request_pacient_of_dep(request):

    if request.method == "POST":
        id = request.POST['id_dep']
    dep = Department.objects.filter(id=id).values('id', 'title')
    req2 = Patient.objects.filter(department=id).values('name', 'doctor__name')
    info = {'request2': req2,
            'dep': dep}
    a = render(request, "request2.html", info)
    return a
