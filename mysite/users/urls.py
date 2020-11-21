from django.urls import include, path
from users.views import (adoptantes,fundacion)
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
	path('reg/', adoptantes.AdoptSignUpView.as_view(),name="registro"),
	path('regf/',fundacion.FundtSignUpView.as_view(),name="registroFundacion"),
	#path('log/',adoptantes.UserLoginView.as_view(),name="login"),
	#path('login/',adoptantes.LoginView.as_view(),name="login"),
	path('l/',auth_views.LoginView.as_view(),{'template_name':'adoptantes/login_1.html'},name="login"),
	path('main/',adoptantes.vista_main,name="main")
	
]