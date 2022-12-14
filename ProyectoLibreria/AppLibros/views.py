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
        autores=Autor.objects.filter(apellido__icontains=apellido)
        libros=Libro.objects.filter(autor__apellido__icontains=apellido)
        if len(autores)!=0:
            return render(request, "AppLibros/resultadoAutores.html", {"autores":autores, "libros":libros})
        else:
            return render(request, "AppLibros/resultadoAutores.html", {"mensaje": f"No hay autores con el apellido {apellido}"})
    else:
        return render(request, "AppLibros/busquedaAutor.html", {"mensaje": "¡No enviaste datos!"})

def libroCrear(request):
    if request.method=="POST":
        miFormulario=LibroFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            _titulo=info["titulo"]
            _isbn=info["isbn"]
            _descripcion=info["descripcion"]
            _fecha_publicacion= info["fecha_publicacion"]
          
            _autor= Autor.objects.get(pk = info["autor"].id)
            _editorial= Editorial.objects.get(pk = info["editorial"].id)

            libro = Libro(titulo = _titulo, isbn = _isbn, descripcion = _descripcion, fecha_publicacion = _fecha_publicacion , autor= _autor, editorial = _editorial)
            libro.save()
            return render(request, "AppLibros/inicio.html", {"mensaje": f"Se creó el libro {_titulo}"})
        else:
            return render(request, "AppLibros/inicio.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
    else:
        miFormulario=LibroFormulario()
        return render(request, "AppLibros/libroCrear.html", {"formulario": miFormulario})

def busquedaLibro(request):
    return render(request, "AppLibros/busquedaLibro.html")

def buscarLibro(request):
    if request.GET["autor"] and request.GET["titulo"]:
        autor=request.GET["autor"]
        titulo=request.GET["titulo"]
        autores=Autor.objects.filter(apellido__icontains=autor)
        libros=Libro.objects.filter(titulo__icontains=titulo, autor__apellido__icontains=autor)
        if len(autores)==0:
            return render(request, "AppLibros/resultadoLibros.html", {"mensajeLibro": f'No hay ningún autor de apellido "{autor}"'})
        elif len(libros)!=0:
            return render(request, "AppLibros/resultadoLibros.html", {"libros":libros})
        else:
            return render(request, "AppLibros/resultadoLibros.html", {"mensajeLibro": f'No hay libros del autor "{autor}" que contengan en su título "{titulo}"'})
    
    if request.GET["autor"]:
        autor=request.GET["autor"]
        libros=Libro.objects.filter(autor__apellido__icontains=autor)
        autores=Autor.objects.filter(apellido__icontains=autor)
        if len(autores)==0:
            return render(request, "AppLibros/resultadoLibros.html", {"mensajeLibro": f'No hay ningún autor de apellido "{autor}"'})
        elif len(libros)!=0:
            return render(request, "AppLibros/resultadoLibros.html", {"libros":libros})
        else:
            return render(request, "AppLibros/resultadoLibros.html", {"mensaje": f'No hay libros del autor "{autor}"'})
    
    elif request.GET["titulo"]:
        titulo=request.GET["titulo"]
        libros=Libro.objects.filter(titulo__icontains=titulo)
        if len(libros)!=0:
            return render(request, "AppLibros/resultadoLibros.html", {"libros":libros})
        else:
            return render(request, "AppLibros/resultadoLibros.html", {"mensaje": f'No hay libros que contengan en su título "{titulo}"'})
    else:
        return render(request, "AppLibros/busquedaLibro.html", {"mensaje": "¡No enviaste datos!"})

def editorialCrear(request):
    if request.method=="POST":
        miFormulario=EditorialFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            nombre=info["nombre"]
            direccion=info["direccion"]
            responsable=info["responsable"]
            email=info["email"]
            editorial=Editorial(nombre=nombre, direccion=direccion, responsable=responsable, email=email)
            editorial.save()
            return render(request, "AppLibros/inicio.html", {"mensaje": f"Se creó la editorial {nombre}"})
        else:
            return render(request, "AppLibros/inicio.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
    else:
        miFormulario=EditorialFormulario()
        return render(request, "AppLibros/editorialCrear.html", {"formulario": miFormulario})

def busquedaEditorial(request):
    return render(request, "AppLibros/busquedaEditorial.html")

def buscarEditorial(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        editoriales=Editorial.objects.filter(nombre__icontains=nombre)
        libros=Libro.objects.filter(editorial__nombre__icontains=nombre)
        if len(editoriales)!=0:
            return render(request, "AppLibros/resultadoEditoriales.html", {"editoriales":editoriales, "libros":libros})
        else:
            return render(request, "AppLibros/resultadoEditoriales.html", {"mensaje": f'No hay editoriales con el nombre "{nombre}"'})
    else:
        return render(request, "AppLibros/busquedaEditorial.html", {"mensaje": "¡No enviaste datos!"})
