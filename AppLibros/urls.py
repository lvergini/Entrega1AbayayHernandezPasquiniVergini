from django.urls import path
from AppLibros import views


urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('autorCrear/', views.autorCrear, name="AutorCrear"),
    path('busquedaAutor/', views.busquedaAutor, name='BusquedaAutor'),
    path('buscar/', views.buscar, name='buscar'),
    path('libroCrear/', views.libroCrear, name="LibroCrear"),
    path('busquedaLibro/', views.busquedaLibro, name='BusquedaLibro'),
    path('buscarLibro/', views.buscarLibro, name='buscarLibro'),
    path('editorialCrear/', views.editorialCrear, name="EditorialCrear"),
    path('busquedaEditorial/', views.busquedaEditorial, name='BusquedaEditorial'),
    path('buscarEditorial/', views.buscarEditorial, name='BuscarEditorial'),
]

