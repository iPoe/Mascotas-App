from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from ..models import usuarios
from ..forms import AdoptSignUpForm

