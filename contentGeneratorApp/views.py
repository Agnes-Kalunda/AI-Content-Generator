from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'landing/index.html', {})


def about(request):
    return render(request, 'landing/about.html', {})

def login(request):
    return render(request, 'authorization/login.html', {})


def register(request):
    return render(request, 'authorization/register.html', {})