from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def guestPage(request):
    return HttpResponse('<h1>GuestPage</h1>')
