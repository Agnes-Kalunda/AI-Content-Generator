from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'layout/landing.html', {})


def about(request):
    return render(request, 'landing/about.html', {})