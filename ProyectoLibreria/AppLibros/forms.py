from django import forms
from AppLibros.models import Editorial, Autor

class AutorFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField(required=False)

class MyAutorChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre + " " + obj.apellido

class MyEditorialChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre

class LibroFormulario(forms.Form):
    titulo= forms.CharField(max_length=30)
    isbn= forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=1000)
    publication_date = forms.DateField()
    autor = MyAutorChoiceField(queryset=Autor.objects.all())
    editorial = MyEditorialChoiceField(queryset=Editorial.objects.all())
    #autor = models.ForeignKey(Autor,on_delete=models.CASCADE)

class EditorialFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    direccion=forms.CharField(max_length=200)
    responsable=forms.CharField(max_length=100)
    email=forms.EmailField()
