from django.urls import path

from proyectoapp.views import (
    socios, 
    libros, 
    juegos, 
    talleres,
    socios_formulario,
    libros_formulario,
    juegos_formulario,
    talleres_formulario,
    busqueda_socios,
    buscar_socios,
    index,
)

urlpatterns = [
    path("socios/", socios, name='socios'),
    path("libros/", libros, name='libros'),
    path("juegos/", juegos, name='juegos'),
    path("talleres/", talleres, name='talleres'),
    path("sociosFormulario/", socios_formulario, name='socios_formulario'),
    path("librosFormulario/", libros_formulario, name='libros_formulario'),
    path("juegosFormulario/", juegos_formulario, name='juegos_formulario'),
    path("talleresFormulario/", talleres_formulario, name='talleres_formulario'),
    path("busquedaSocios/", busqueda_socios, name='busqueda_socios'),
    path("buscar/", buscar_socios, name='buscar_socios'),
    path('', index, name='index'),
]