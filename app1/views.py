from django.shortcuts import render

# Create your views here.
from app1.forms import *
from app1.models import *
def insert_student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            sname=SFDO.cleaned_data['sname']
            sid=SFDO.cleaned_data['sid']
            semail=SFDO.cleaned_data['semail']
            so=Student.objects.get_or_create(sname=sname,sid=sid,semail=semail)[0]
            so.save()
            qso=Student.objects.all()
            d={'qso':qso}
            return render(request,'display_student.html',d)
    return render(request,'insert_student.html',d)