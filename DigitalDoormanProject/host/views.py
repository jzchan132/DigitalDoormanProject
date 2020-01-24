from django.shortcuts import render
from django.http import HttpResponse
from .models import Event


# Create your views here.
def createEvent(request):
    return render(request, 'host/createEvent.html')

def viewEvent(request):
    context = {
        'events': Event.objects.all()
        }
    return render(request, 'host/viewEvent.html', context)
