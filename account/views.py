from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request) :
    return render(request,'account/login.html')

def register(request) :
    if request.method == 'POST':
        if request.POST['ps1'] == request.POST['ps2'] :
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'account/register.html',{'error':'nama sudah terpakai'})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'],password = request.POST['ps1'])
                auth.login(request,user)
                return redirect('login')
        else:
            return render(request,'account/register.html',{'errorps':'password tidak sama'})
    else :
        return render(request,'account/register.html')
