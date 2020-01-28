from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from .forms import NewEventForm
from django.http import Http404

# Create your views here.
def createEvent(request):
    newEvent = NewEventForm(request.POST)
    if newEvent.is_valid():
        new_event = newEvent.save(commit=False)
        new_event.hostUser = request.user
        new_event.save()
        return redirect('homePage')
    else:
        newEvent = NewEventForm(request.POST)

    return render(request, 'host/createEvent.html', {'form':newEvent})

def viewEvent(request):
    context = {
        'events': Event.objects.all()
        }
    return render(request, 'host/viewEvent.html', context)
