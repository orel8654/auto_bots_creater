from django.views.generic import TemplateView

class Payment(TemplateView):
    template_name = 'payment/qiwi_form.html'
    #Настроить уведомления о получении денежных средств после деплоя на домене или открытом IP
class Verify(TemplateView):
    pass
