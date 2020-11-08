from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from ..models import User
from ..forms import AdoptSignUpForm


class AdoptSignUpView(CreateView):
    model = User
    form_class = AdoptSignUpForm
    template_name = 'adoptantes/registro_adop.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'adoptante'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('adoptantes:main')

@login_required(login_url='usuarios:login')
def vista_main(request):
    context = {}
    return render(request,'adoptantes/main.html',context)