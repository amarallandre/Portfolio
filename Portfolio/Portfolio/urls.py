from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

urlpatterns = [
    path('', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
]