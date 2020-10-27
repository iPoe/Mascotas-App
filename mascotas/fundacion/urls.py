from django.urls import path

from . import views

app_name = 'fundacion'

urlpatterns = [
	path('fund_registro/', views.registro,name="registro"),

]
