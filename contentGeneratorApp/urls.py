from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about-aggie-ai', views.about, name='about')
]   