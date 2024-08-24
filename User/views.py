from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from User.forms import RegistrationForm


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        if self.request.user.role is not None:
            if self.request.user.role.name == 'Admin':
                return reverse_lazy('index')
            else:
                return reverse_lazy('menu_list')
        else:
            return reverse_lazy('menu_list')

class RegisterView(CreateView):
    template_name = 'auth/register.html'
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse_lazy('menu_list')

