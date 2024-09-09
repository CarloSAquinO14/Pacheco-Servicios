from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")
def inicio(request):
    return render(request,"inicio.html")
def contacto(request):
    return render(request,"contacto.html")
def producto(request):
    return render(request,"producto.html")
def servicios(request):
    return render(request,"servicios.html")

