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
	for registros in registroSensores:	
		tmp = {
			'id': str(x),
			'sensor1': registros.Sensor1,
			'sensor2': registros.Sensor2,
			'idLocal':registros.idLocal,
		}
		registroSensores_json.append(tmp)
	return JsonResponse(registroSensores_json, safe = False)

def get_ultimos_registro_sensores(request):
	registroSensores_json = []
	registroSensores = RegistroSensores.objects.all()
	for registros in registroSensores:	
		tmp = {
			'id': str(x),
			'sensor1': registros.Sensor1,
			'sensor2': registros.Sensor2,
			'idLocal':registros.idLocal,
		}
		registroSensores_json.append(tmp)
	return JsonResponse(registroSensores_json, safe = False)

def leerTxt(request):
	registroSensores_json = []
	data=urlopen('https://nuestrabodalyo.000webhostapp.com/datos.txt')
	x=[]
	cadenaid=""
	if data=="":
		print("Sin información")
	for line in data:
		#print(line[0:len(line)-1])
		a=str(line)
		x = a.split(",")
		fecha=x[0] 
		fecha=fecha[2:len(fecha)]

		registroSensores = RegistroSensores.objects.filter(idLocal=x[5])

		if len(registroSensores)>0:
			print("ya registrado " + x[5])
		else:
			informacion=RegistroSensores(
				Fecha=x[1],#time.strftime("%Y/%m/%Y"),
				Hora=x[2],
				Sensor1=x[3],
				Sensor2=x[4],
				idLocal=x[5])
			informacion.save()
			if cadenaid=="":
				cadenaid=cadenaid + x[5]
			else:
				cadenaid=cadenaid +","+ x[5]
			print("guardado " + x[5])
		registroSensores_json={'id':cadenaid
		}
	return HttpResponse(cadenaid)
