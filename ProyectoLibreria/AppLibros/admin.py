from django.contrib import admin
from .models import Autor, Editorial, Libro

# Register your models here.

admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Libro)