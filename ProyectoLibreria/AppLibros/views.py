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



def libroCrear(request):
    if request.method=="POST":
        miFormulario=LibroFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            _titulo=info["titulo"]
            _isbn=info["isbn"]
            _descripcion=info["descripcion"]
            _publication_date= info["publication_date"]
          
            _autor= Autor.objects.get(pk = info["autor"].id)
            _editorial= Editorial.objects.get(pk = info["editorial"].id)

            libro = Libro(titulo = _titulo, isbn = _isbn, descripcion = _descripcion, publication_date = _publication_date , autor= _autor, editorial = _editorial)
            libro.save()
            return render(request, "AppLibros/inicio.html", {"mensaje": f"Se creó el libro {_titulo}"})
        else:
            return render(request, "AppLibros/inicio.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
    else:
        miFormulario=LibroFormulario()
        return render(request, "AppLibros/libroCrear.html", {"formulario": miFormulario})

