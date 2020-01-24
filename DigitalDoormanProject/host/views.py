from django.shortcuts import render
from django.http import HttpResponse

guests = [
    {
        'guestName': 'Ruth poop asdfa sdf',
        'ID': '1',
        'tokens': '1'
        },
    {
        'guestName': 'Michelliot',
        'ID': '2',
        'tokens': '1'
        },
    {
        'guestName': 'Gummy Bear',
        'ID': '3',
        'tokens': '1'
        }
    ]




# Create your views here.
def createEvent(request):
    return render(request, 'host/createEvent.html')

def guestList(request):
    context = {
        'guests': guests
        }
    return render(request, 'host/guestList.html', context)