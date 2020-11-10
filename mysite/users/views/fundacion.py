from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from ..models import usuarios
from ..forms import FundacionSignUpForm

class FundtSignUpView(CreateView):
    model = usuarios
    form_class = FundacionSignUpForm
    template_name = 'fundaciones/registro_f.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'fundacion'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #print(user)
        login(self.request, user)
        return redirect('users:main')