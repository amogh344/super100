from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def landingPageView(request):
    return HttpResponse("Hello, this is the landing page of app1.")