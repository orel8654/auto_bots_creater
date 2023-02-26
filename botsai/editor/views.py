from django.views.generic import TemplateView, FormView
from .forms import TemplatesForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import TelegramBots
from django.http import HttpResponseRedirect

class Editor(FormView):
    template_name = 'editor/editor_page.html'
    form_class = TemplatesForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        super(Editor, self).form_valid(form)
        data = form.cleaned_data
        owner = User.objects.get(username=self.request.user.username)
        data['owner'] = owner
        TelegramBots.objects.create(**data)
        return HttpResponseRedirect(self.success_url)
class CreaterTemplateTelegramBot(TemplateView):
    template_name = 'editor/editor_configuration.html'