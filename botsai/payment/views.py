from django.views.generic import TemplateView

class Payment(TemplateView):
    template_name = 'payment/qiwi_form.html'
