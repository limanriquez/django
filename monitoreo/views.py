from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
from monitoreo.serializers import *
from monitoreo.views import *
from urllib.request import urlopen
from monitoreo.models import *
import time
# Create your views here.
@login_required()
def inicio(request):
	context={
		"title":"Hola mundo",
	}
	return render (request,"inicio.html", context)

class RegistroSensoresViewSet(viewsets.ModelViewSet):
	queryset=RegistroSensores.objects.all()
	serializer_class=RegistroSensoresSerializer

#@login_required()
def get_registro_sensores(request):
	registroSensores_json = []
	registroSensores = RegistroSensores.objects.all()
	x=0
	for registros in registroSensores:
		#'Hora':registros.Hora,
		#'Sensor2':registros.Sensor2,
		#'Id':registros.Id,
		x=x+1
		tmp = {
			'y': str(x),
			'a': registros.Sensor1,
			'b': registros.Sensor2,
		}
		registroSensores_json.append(tmp)
	return JsonResponse(registroSensores_json, safe = False)

def leerTxt(request):
	registroSensores_json = []
	data=urlopen('https://nuestrabodalyo.000webhostapp.com/datos.txt')
	x=[]
	for line in data:
		#print(line[0:len(line)-1])
		a=str(line)
		x = a.split(",")
		fecha=x[0] 
		fecha=fecha[2:len(fecha)]
		informacion=RegistroSensores(
			Fecha=x[1],#time.strftime("%Y/%m/%Y"),
			Hora=x[2],
			Sensor1=x[3],
			Sensor2=x[4])
		informacion.save()
	return JsonResponse(registroSensores_json, safe = False)
