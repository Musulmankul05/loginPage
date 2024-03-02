from uuid import uuid4

from django.contrib import auth
from django.http import HttpResponseRedirect

from .models import UserModel
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView


class SuccessView(TemplateView):
    template_name = 'success.html'

    def get(self, request, *args, **kwargs):
        uuid_code = kwargs.get('uuid')
        return render(request, self.template_name, {'uuid': uuid_code})


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['username'] = self.request.user
        return context


class LoginPageView(LoginView):
    model = UserModel
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        uuid_code = str(uuid4())
        success_url = reverse_lazy('loginApp:success', kwargs={'uuid': uuid_code})
        return success_url


class RegisterView(CreateView):
    model = UserModel
    template_name = 'registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('loginApp:login')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('loginApp:index'))
