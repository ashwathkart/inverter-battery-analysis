from django.shortcuts import render
from django.http import HttpResponse
from .models import Battery

# Create your views here.

# def battery(request):
#     rec = Battery_1.objects.get(id__exact=numb)
#     return render(request, 'battery.html')

def test(request, number):
    return HttpResponse('<h1> Welcome, {} </h1>'.format(number))