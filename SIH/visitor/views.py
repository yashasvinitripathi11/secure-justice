from django.shortcuts import render
from .models import Commons_law,Children_law,Mens_law,Women_law,Transgender_law

def CL(request): 
    Commons_laws = Commons_law.objects.all()
    a=str()
    for i in Commons_laws:
        a+=(i.content) 
    parameter={
        'Commons_laws':a.split(".")
    }
    return render(request,'visitor/CL.html',parameter)

def CLR(request):
    Child_laws = Children_law.objects.all()
    a=str()
    for i in Child_laws:
        a+=(i.content) 
    parameter={
        'Child_laws':a.split(".")
    }
    return render(request,'visitor/CLR.html',parameter)

def MLR(request):
    Mens_laws = Mens_law.objects.all()
    a=str()
    for i in Mens_laws:
        a+=(i.content) 
    parameter={
        'Mens_laws':a.split(".")
    }
    return render(request,'visitor/MLR.html',parameter)

def TLR(request):
    Transgender_laws = Transgender_law.objects.all()
    a=str()
    for i in Transgender_laws:
        a+=(i.content) 
    parameter={
        Transgender_laws:a.split(".")
    }
    return render(request,'visitor/TLR.html',parameter)

def WLR(request):
    Women_laws = Women_law.objects.all()
    a=str()
    for i in Women_laws:
        a+=(i.content) 
    parameter={
        Women_laws:a.split(".")
    }
    return render(request,'visitor/WLR.html',parameter)
