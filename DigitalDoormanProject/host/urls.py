from django.urls import path
from . import views

urlpatterns = [
    path('createEvent/', views.createEvent, name='host home'),
    path('viewEvent/', views.viewEvent, name='event view'),
    path('guestList/', views.guestList, name='guest list'),
]