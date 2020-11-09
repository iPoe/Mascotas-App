from django.urls import include, path
from users.views import adoptantes

app_name = 'users'

urlpatterns = [
	path('reg/', adoptantes.AdoptSignUpView.as_view(),name="registro"),
	path('main/',adoptantes.vista_main,name="main")
	
]