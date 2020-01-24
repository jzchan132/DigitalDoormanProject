from django.urls import path
from . import views

urlpatterns = [
    path('createEvent/', views.createEvent, name='host home'),
    path('guestList/', views.guestList, name='guestList'),
]