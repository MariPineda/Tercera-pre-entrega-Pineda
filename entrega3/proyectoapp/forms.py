from django import forms

class SociosFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    socio = forms.IntegerField()
    activo = forms.BooleanField(required=False)

class LibrosFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=60)
    edadRecomendada = forms.IntegerField()

class JuegosFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=60)
    edadRecomendada = forms.IntegerField()

class TalleresFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    nivel = forms.CharField(max_length=20)
    camada = forms.IntegerField()

class BusquedaSocios(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    socio = forms.IntegerField()
    activo = forms.BooleanField()