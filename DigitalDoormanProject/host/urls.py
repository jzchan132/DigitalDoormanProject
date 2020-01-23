from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='host home'),
    path('about/', views.about, name='about'),
]