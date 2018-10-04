from django.contrib import admin

# Register your models here.
from .models import RegistroSensores
class AdminRegistroSensores(admin.ModelAdmin):
	list_display=["Fecha","Hora","Sensor1","Sensor2"]
	lsit_filter=["Fecha","Hora","Sensor1","Sensor2"]
	lidt_editable=["Fecha","Hora","Sensor1","Sensor2"]
	search_fields=["Fecha","Hora","Sensor1","Sensor2"]
	class Meta:
		model:RegistroSensores

admin.site.register(RegistroSensores, AdminRegistroSensores)