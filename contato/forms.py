from django import forms

from .models import Contato
from simoes_tecnologia.content import CONTACT_SOLUTION_CHOICES


class ContatoForm(forms.ModelForm):
    recaptcha_token = forms.CharField(widget=forms.HiddenInput(), required=False)
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={"tabindex": "-1", "autocomplete": "off"}))

    class Meta:
        model = Contato
        fields = ["name", "organization", "email", "whatsapp", "solution_type", "message"]
        labels = {
            "name": "Nome",
            "organization": "Empresa ou organização",
            "email": "E-mail",
            "whatsapp": "WhatsApp",
            "solution_type": "Tipo de solução",
            "message": "Mensagem",
        }
        error_messages = {
            "name": {"required": "Informe seu nome."},
            "organization": {"required": "Informe a empresa ou organização."},
            "email": {
                "required": "Informe seu e-mail.",
                "invalid": "Informe um e-mail válido.",
            },
            "whatsapp": {"required": "Informe um WhatsApp para contato."},
            "solution_type": {"required": "Escolha o tipo de solução."},
            "message": {"required": "Conte brevemente o que você precisa resolver."},
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Seu nome",
                "autocomplete": "name",
                "required": True,
            }),
            "organization": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Empresa, condomínio, igreja, evento ou organização",
                "autocomplete": "organization",
                "required": True,
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-input",
                "placeholder": "seuemail@exemplo.com",
                "autocomplete": "email",
                "required": True,
            }),
            "whatsapp": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "(00) 00000-0000",
                "autocomplete": "tel",
                "inputmode": "tel",
                "required": True,
            }),
            "solution_type": forms.Select(
                choices=[("", "Selecione uma opção"), *CONTACT_SOLUTION_CHOICES],
                attrs={"class": "form-input form-select", "required": True},
            ),
            "message": forms.Textarea(attrs={
                "class": "form-textarea",
                "placeholder": "Descreva o processo, problema ou ideia que você quer organizar.",
                "rows": 6,
                "required": True,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["organization"].required = True
        self.fields["whatsapp"].required = True
        self.fields["solution_type"].choices = [("", "Selecione uma opção"), *CONTACT_SOLUTION_CHOICES]

    def clean_website(self):
        website = self.cleaned_data.get("website", "")
        if website:
            raise forms.ValidationError("Não foi possível enviar a mensagem.")
        return website

    def save(self, commit=True):
        self.cleaned_data.pop("recaptcha_token", None)
        self.cleaned_data.pop("website", None)
        return super().save(commit=commit)
