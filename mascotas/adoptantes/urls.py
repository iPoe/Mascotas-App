from django.urls import path

from . import views

app_name = 'adoptantes'

urlpatterns = [
	path('registro/', views.vista_registro_adoptante.as_view(),name="registro"),
	path('login_adop/', views.LoginView.as_view(),name="login"),
	path('home/',views.vista_main,name="main"),
	#path('log/',views.test_login.as_view(),name="login")
]