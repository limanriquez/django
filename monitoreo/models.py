from django.db import models

# Create your models here.
class RegistroSensores(models.Model):
	Id=models.AutoField(primary_key=True)
	Fecha=models.DateField()
	Hora=models.CharField(max_length=50)
	Sensor1=models.FloatField()
	Sensor2=models.FloatField()
	idLocal=models.IntegerField(null=True)

	def __unicode__(self):
		return self.Hora

	def __str__(self):
		return self.Hora