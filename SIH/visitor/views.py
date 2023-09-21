from django.shortcuts import render
from .models import Commons_law,Children_law,Mens_law,Women_law,Transgender_law

def CL(request): 
    Commons_laws = Commons_law.objects.all()
    parameter={
        'Commons_laws':Commons_laws
    }
    return render(request,'visitor/CL.html',parameter)

def CLR(request):
    Child_laws = Children_law.objects.all()
    parameter={
        'Child_laws':Child_laws
    }
    return render(request,'visitor/CLR.html',parameter)

def MLR(request):
    Mens_laws = Mens_law.objects.all()
    parameter={
        'Mens_laws':Mens_laws
    }
    return render(request,'visitor/MLR.html',parameter)

def TLR(request):
    Transgender_laws = Transgender_law.objects.all()
    parameter={
        'Transgender_laws':Transgender_laws
    }
    return render(request,'visitor/TLR.html',parameter)

def WLR(request):
    Women_laws = Women_law.objects.all()
    parameter={
        'Women_laws':Women_laws
    }
    return render(request,'visitor/WLR.html',parameter)
