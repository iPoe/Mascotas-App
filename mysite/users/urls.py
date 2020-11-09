from django.urls import include, path
from users.views import (adoptantes,fundacion)

app_name = 'users'

urlpatterns = [
	path('reg/', adoptantes.AdoptSignUpView.as_view(),name="registro"),
	path('regf/',fundacion.FundtSignUpView.as_view(),name="registroFundacion"),
	path('main/',adoptantes.vista_main,name="main")
	
]