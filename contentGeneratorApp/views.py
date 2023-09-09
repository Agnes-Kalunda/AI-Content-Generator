from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages 
# Create your views here.
def home(request):
    return render (request, 'landing/index.html', {})


def about(request):
    return render(request, 'landing/about.html', {})

def login(request):
    return render(request, 'authorization/login.html', {})


def register(request):
   
    if request.method == 'POST':
        email= request.POST['email'].replace('','').lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not password1 == password2:
            messages.error(request,'Passwords do not match')
       
        if User.objects.filter(email=email).exists():
            messages.error(request, "A user with the email address : {} already exists, please use a different email".format(email))

        return redirect('register')
    return render(request, 'authorization/register.html', {})