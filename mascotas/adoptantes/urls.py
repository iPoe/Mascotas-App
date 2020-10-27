from django.urls import path

from . import views

app_name = 'adoptantes'

urlpatterns = [
	path('registro/', views.pag_registro,name="registro"),
	path('login/', views.login_adoptante,name="login"),


]