from django.views.generic import FormView, TemplateView
from .forms import RegForms

class AuthPage(FormView):
    template_name = 'auth_page/auth_page.html'

class RegPage(FormView):
    template_name = 'auth_page/reg_page.html'
    form_class = RegForms
    success_url = '/account/succes/'

    def form_valid(self, form):
        return super().form_valid(form)

class SuccesReg(TemplateView):
    template_name = 'auth_page/reg_page.html'