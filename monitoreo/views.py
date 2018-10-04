from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
from monitoreo.serializers import *
from monitoreo.views import *
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