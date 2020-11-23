from django.conf.urls import url
from django.urls import include, path
from users.views import (adoptantes,fundacion)
from django.contrib.auth import views as auth_views
from users.forms import UserloginForm

app_name = 'users'

urlpatterns = [
	path('reg/', adoptantes.AdoptSignUpView.as_view(),name="registro"),
	path('regf/',fundacion.FundtSignUpView.as_view(),name="registroFundacion"),
	path('log/',adoptantes.loginPage,name="login"),
	path('main2/',adoptantes.vista_main_2,name="main2"),
	path('l/',adoptantes.logoutUser,name="logout"),

	path('main/',adoptantes.vista_main,name="main")
	
]