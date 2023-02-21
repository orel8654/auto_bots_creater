from django.views.generic import TemplateView

class GeneralPage(TemplateView):
    template_name = 'general_page/general_page.html'