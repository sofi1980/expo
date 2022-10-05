from django.contrib import admin

from .models import Categoria,Producto
class CategoriaAdmin(admin.ModelAdmin):
    list_display =['id','descripCategoria']

admin.site.register(Categoria,CategoriaAdmin)

admin.site.register(Producto)
