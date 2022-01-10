from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
# Create your views here.
from django.views.generic import CreateView

class SignUpView(CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'