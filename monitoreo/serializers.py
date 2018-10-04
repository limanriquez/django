from rest_framework import serializers
from monitoreo.models import *

class RegistroSensoresSerializer(serializers.ModelSerializer):
	class Meta:
		model=RegistroSensores
		exclude=[]