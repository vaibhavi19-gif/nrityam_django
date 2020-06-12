from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Cinfo


def signup(request):

    if request.method == 'POST':
        Fullname = request.POST['Fullname']
        Email = request.POST['Email']
        Username = request.POST['Username']
        Password = request.POST['Password']
        Confirm = request.POST['Confirm']

        if Password == Confirm:
            if Cinfo.objects.filter(Username=Username).exists():
                messages.info(request, "Username taken")
                return redirect('signup')
            elif Cinfo.objects.filter(Email=Email).exists():
                messages.info(request, "Email taken")
                return redirect('signup')
            else:
                c = Cinfo(Username=Username,Password=Password,Email=Email,Fullname=Fullname)
                c.save()
                user = User.objects.create_user(username=Username, password=Password, email=Email, first_name=Fullname)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')
        else:
            messages.info(request, "Password not matching..")
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def login(request):

    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']

        user = auth.authenticate(username=Username,password=Password)
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
