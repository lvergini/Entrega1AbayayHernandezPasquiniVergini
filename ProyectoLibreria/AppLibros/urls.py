from django.urls import path
from AppLibros import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
]

