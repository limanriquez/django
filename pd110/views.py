from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from monitoreo.serializers import *
@login_required()
def home(request):
	context={
		"title":"Hola mundo",
	}
	return render (request,"home.html", context)