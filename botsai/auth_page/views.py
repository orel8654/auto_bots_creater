from django.views.generic import FormView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import *

class AuthPage(FormView):
    template_name = 'auth_page/auth_page.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')
    failed_url = reverse_lazy('login')

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect(self.failed_url)

class RegPage(CreateView):
    template_name = 'auth_page/reg_page.html'
    form_class = RegForms
    success_url = reverse_lazy('login')

class Logout(TemplateView):
    template_name = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return HttpResponseRedirect(self.template_name)