from django.contrib import admin

from proyectoapp.models import (
    Socios,
    Libros,
    Juegos,
    Talleres
)

admin.site.register(Socios)
admin.site.register(Libros)
admin.site.register(Juegos)
admin.site.register(Talleres)
