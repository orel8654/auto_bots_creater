from django import forms

class RegForms(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()

    def send_email(self):
        fields = self.changed_data
        pass