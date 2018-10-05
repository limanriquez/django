from django.conf.urls import url, include
from monitoreo.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'RegistroSensores',RegistroSensoresViewSet)
#api/v1/RegistroSensores
RegistroSensoresViewSet
urlpatterns=[
	url(r'^api/v1/', include(router.urls)),
	url(r'inicio$',inicio,name='inicio'),
	url(r'^get_registro_sensores/$', get_registro_sensores, name="get_registro_sensores"),
	#url(r'accounts/login/$',inicio,name='inicio'),
]