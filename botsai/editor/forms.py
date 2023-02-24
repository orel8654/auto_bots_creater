from django import forms
from .models import TelegramBots

class TemplatesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_bot'].empty_label = 'Тип не выбран'
        self.fields['type_bot'].widget.attrs['class'] = 'form-creatertp'

    class Meta:
        model = TelegramBots
        fields = ['name', 'name_bot', 'api_token', 'type_bot']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-creatertp'}),
            'name_bot': forms.TextInput(attrs={'class': 'form-creatertp'}),
            'api_token': forms.TextInput(attrs={'class': 'form-creatertp'}),
        }