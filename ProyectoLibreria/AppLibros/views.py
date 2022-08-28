from django.shortcuts import render
from django.http import HttpResponse
from AppLibros.forms import *
from AppLibros.models import *

# Create your views here.
def inicio(request):
      return render(request, "AppLibros/inicio.html")

def autorCrear(request):
    if request.method=="POST":
        miFormulario=AutorFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            autor=Autor(nombre=nombre, apellido=apellido, email=email)
            autor.save()
            return render(request, "AppLibros/inicio.html", {"mensaje": f"Se creó el autor {nombre} {apellido}"})
        else:
            return render(request, "AppLibros/inicio.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
    else:
        miFormulario=AutorFormulario()
        return render(request, "AppLibros/autorCrear.html", {"formulario": miFormulario})

def busquedaAutor(request):
    return render(request, "AppLibros/busquedaAutor.html")

def buscar(request):
    if request.GET["apellido"]:
        apellido=request.GET["apellido"]
        autores=Autor.objects.filter(apellido=apellido)
        if len(autores)!=0:
            return render(request, "AppLibros/resultadoAutores.html", {"autores":autores})
        else:
            return render(request, "AppLibros/resultadoAutores.html", {"mensaje": f"No hay autores con el apellido {apellido}"})
    else:
        return render(request, "Appcoder/busquedaAutor.html", {"mensaje": "No enviaste datos!"})


