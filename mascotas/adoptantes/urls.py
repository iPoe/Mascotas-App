from django.urls import path

from . import views

app_name = 'adoptantes'

urlpatterns = [
	path('registro/', views.pag_registro_adoptante,name="registro"),
	path('login_adop/', views.login_adoptante,name="login"),
	path('',views.vista_main,name="test"),
]