from django.shortcuts import render

def CL(request):
    return render(request,'visitor/CL.html')

def CLR(request):
    return render(request,'visitor/CLR.html')

def MLR(request):
    return render(request,'visitor/MLR.html')

def TLR(request):
    return render(request,'visitor/TLR.html')

def WLR(request):
    return render(request,'visitor/WLR.html')
