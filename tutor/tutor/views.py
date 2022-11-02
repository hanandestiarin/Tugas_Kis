from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("ini about")

def articless(request,year):
    year=year
    str = year
    
    return HttpResponse(year)