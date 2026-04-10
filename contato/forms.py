from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    recaptcha_token = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Contato
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Seu nome',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Seu email',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Sua mensagem',
                'rows': 5,
                'required': True
            }),
        }

    def save(self, commit=True):
        # Remove o campo recaptcha_token antes de salvar
        self.cleaned_data.pop('recaptcha_token', None)
        return super().save(commit=commit)


