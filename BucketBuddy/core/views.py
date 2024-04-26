from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
        return render(request,"index.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password= password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Info')
            return redirect('login')
           
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        pass
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('register')
        
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('register')
        
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model, id_user = user_model.id)
            new_profile.save()
            return redirect('login')

    else:
        return render(request,'register.html')

