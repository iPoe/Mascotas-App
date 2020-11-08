from django.urls import include, path
from usuarios.views import adoptantes

app_name = 'usuarios'

urlpatterns = [
	path('reg/', adoptantes.AdoptSignUpView.as_view(),name="registro"),
	path('main/',adoptantes.vista_main,name="main")
	
]

#{% url 'adoptantes:login' %}