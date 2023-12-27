from django.shortcuts import render

from django.http import HttpResponse
from proyectoapp.models import Socios, Libros, Juegos, Talleres
from proyectoapp.forms import SociosFormulario, LibrosFormulario, JuegosFormulario, TalleresFormulario, BusquedaSocios

def index(request):
    
    formulario = BusquedaSocios()
    return render(request, 'busqueda_socios.html', {"formulario" : formulario})

def socios(request):

    return render(request, 'socios.html')

def libros(request):

    return render(request, 'libros.html')

def juegos(request):
    return render(request, 'juegos.html')

def talleres(request):
    return render(request, 'talleres.html')

def socios_formulario(request):

    if request.method == "POST":
        formulario = SociosFormulario(request.POST)
        print("is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            email = datos.get("email")
            socio = datos.get("socio")
            activo = datos.get("activo")

            socios = Socios(nombre=nombre, apellido=apellido, email=email, socio=socio, activo=activo)
            socios.save()
            return render(request, 'index.html')
        
    else:
        formulario = SociosFormulario()
        return render(request, 'socios_formulario.html', {"formulario": formulario})
    
    
def libros_formulario(request):

    if request.method == "POST":
        formulario = LibrosFormulario(request.POST)
        print("is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data
            titulo = datos.get("titulo")
            tipo = datos.get("tipo")
            edadRecomendada = datos.get("edadRecomendada")

            libros = Libros(titulo=titulo, tipo=tipo, edadRecomendada=edadRecomendada)
            libros.save()
            return render(request, 'index.html')
        
    else:
        formulario = LibrosFormulario()
        return render(request, 'libros_formulario.html', {"formulario": formulario})
    

def juegos_formulario(request):

    if request.method == "POST":
        formulario = JuegosFormulario(request.POST)
        print("is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nombre = datos.get("nombre")
            tipo = datos.get("tipo")
            edadRecomendada = datos.get("edadRecomendada")

            juegos = Juegos(nombre=nombre, tipo=tipo, edadRecomendada=edadRecomendada)
            juegos.save()
            return render(request, 'index.html')
        
    else:
        formulario = JuegosFormulario()
        return render(request, 'juegos_formulario.html', {"formulario": formulario})
    

def talleres_formulario(request):

    if request.method == "POST":
        formulario = TalleresFormulario(request.POST)
        print("is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nombre = datos.get("nombre")
            nivel= datos.get("nivel")
            camada = datos.get("camada")

            talleres = Talleres(nombre=nombre, nivel=nivel, camada=camada)
            talleres.save()
            return render(request, 'index.html')
        
    else:
        formulario = TalleresFormulario()
        return render(request, 'talleres_formulario.html', {"formulario": formulario})


def busqueda_socios(request):
    
    if request.method == "GET":
        
        socio = request.GET.get("socio")

        if socio is None:
            return HttpResponse("Debe enviar un socio")
        
        socio = Socios.objects.filter(socio=socio)
        
        return render(request, 'busqueda_socios_respuesta.html', {"socio": socio})
        
        

def buscar_socios(request):

    if request.method == "GET":
        
        socio = request.GET.get("socio")
      
        if socio is None:
            return HttpResponse("Enviar el socio a buscar")
        socio= Socios.objects.filter(socio__icontains=socio)
        #print(socio)
        #return HttpResponse(f"Se buscó el socio número: {socio}")

        return render (request,'busqueda.html', {"socio" : socio})
  





"""def socios_formulario(request):

    if request.method == "POST":
            
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        socio = request.POST.get("socio")
        activo = request.POST.get("activo")

        print(f"El socio cargado es {nombre} {apellido} y su número de socio es {socio}")

        socios = Socios(nombre=nombre, apellido=apellido, email=email, socio=socio, activo=activo)
        socios.save()

        return render(request,'index.html')
        
    return render(request, 'socios_formulario.html')



def libros_formulario(request):

    if request.method == "POST":

        titulo = request.POST.get("titulo")
        tipo = request.POST.get("tipo")
        edadRecomendada = request.POST.get("edadRecomendada")

        print(f"El título del libro es: {titulo}, el tipo de libro es {tipo} y su lectura es recomendada a partir de {edadRecomendada} años")

        libros = Libros(titulo=titulo, tipo=tipo, edadRecomendada=edadRecomendada)
        libros.save()

        return render(request,'index.html')

    return render(request, 'libros_formulario.html')


def juegos_formulario(request):

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        tipo = request.POST.get("tipo")
        edadRecomendada = request.POST.get("edadRecomendada")

        print(f"El título del juego es: {nombre}, es del tipo {tipo} para jugar a partir de {edadRecomendada} años")

        juegos = Juegos(nombre=nombre, tipo=tipo, edadRecomendada=edadRecomendada)
        juegos.save()

        return render(request,'index.html')

    return render(request, 'juegos_formulario.html')
  

def talleres_formulario(request):

    if request.method == "POST":
        
        nombre = request.POST.get("nombre")
        nivel = request.POST.get("nivel")
        camada = request.POST.get("camada")

        print(f"El nombre del taller es: {nombre}, nivel {nivel} de la camada {camada}")

        talleres = Talleres(nombre=nombre, nivel=nivel, camada=camada)
        talleres.save()

        return render(request,'index.html')

    return render(request, 'talleres_formulario.html')
"""