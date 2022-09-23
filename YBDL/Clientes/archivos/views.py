from .models import Recibos, Facturas, Retenciones, reclamo
from django.shortcuts import render
from django.http import HttpResponse

def buscar(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        if Facturas.objects.filter(nombre__contains=nombre):
            Facturas = Facturas.objects.filter(nombre__contains=nombre)
            return render(request,"buscar.html",{"Facturas":Facturas})
        elif Recibos.objects.filter(nombre__contains=nombre):
            Recibos = Recibos.objects.filter(nombre__contains=nombre)
            return render(request,"buscar.html",{"Recibos":Recibos})
        elif reclamo.objects.filter(nombre__contains=nombre):
            reclamo = reclamo.objects.filter(nombre__contains=nombre)
            return render(request,"buscar.html",{"reclamo":reclamo})
        else:    
            return HttpResponse("material no encontrado")
    return render(request,"buscar.html")

def insertar_clientes(request):
    if request.method == "POST":
        datos = clientes(fecha_de_emision = request.POST["fecha_de_emision"],clientes = request.POST["cliente"],nombre=request.POST["nombre"],link=request.POST["link"])
        datos.save()
        return render(request,"insertar_clientes.html")
    return render(request,"insertar_clientes.html")

def insertar_recibos(request):
    if request.method == "POST":
        datos = recibos(fecha_de_emision = request.POST["fecha_de_emision"],Recibos = request.POST["recibos"],nombre=request.POST["nombre"],link=request.POST["link"])
        datos.save()
        return render(request,"insertar_recibos.html")
    return render(request,"insertar_recibos.html")

def insertar_reclamo(request):
    if request.method == "POST":
        datos = reclamo(fecha_de_emision = request.POST["fecha_de_emision"],reclamo= request.POST["reclamo"],nombre=request.POST["nombre"],link=request.POST["link"])
        datos.save()
        return render(request,"insertar_reclamo.html")
    return render(request,"insertar_reclamo.html")
# Create your views here.
