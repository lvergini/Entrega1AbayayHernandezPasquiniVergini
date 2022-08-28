from django.urls import path
from AppLibros import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('autorCrear/', views.autorCrear, name="AutorCrear"),
    path('busquedaAutor/', views.busquedaAutor, name='BusquedaAutor'),
    path('buscar/', views.buscar, name='buscar'),
    path('libroCrear/', views.libroCrear, name="LibroCrear")
]

