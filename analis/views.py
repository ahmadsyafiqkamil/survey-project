from django.shortcuts import render

# Create your views here.
def dashboard(request) :
    return render(request,'dashboard/dashboard.html')

def organisasi(request) :
    return render(request,'dashboard/organisasi.html')

def perangkat(request) :
    return render(request,'dashboard/perangkat.html')
