import json
from urllib import parse, request
from urllib.error import URLError

from django.conf import settings
from django import forms

from .models import Contato
from simoes_tecnologia.content import CONTACT_SOLUTION_CHOICES


SPAM_MESSAGE_INDICATORS = (
    "collect-cryptocurrency",
    "cryptocurrency",
    "reviewing crypto",
    "earn $",
    "per day",
    "message-id",
    "telegra.ph",
)


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
        self.remote_ip = kwargs.pop("remote_ip", None)
        super().__init__(*args, **kwargs)
        self.fields["organization"].required = True
        self.fields["whatsapp"].required = True
        self.fields["solution_type"].choices = [("", "Selecione uma opção"), *CONTACT_SOLUTION_CHOICES]

    def clean_website(self):
        website = self.cleaned_data.get("website", "")
        if website:
            raise forms.ValidationError("Não foi possível enviar a mensagem.")
        return website

    def clean_message(self):
        message = self.cleaned_data.get("message", "")
        normalized_message = message.lower()
        spam_score = sum(1 for item in SPAM_MESSAGE_INDICATORS if item in normalized_message)
        link_count = normalized_message.count("http://") + normalized_message.count("https://")

        if spam_score >= 2 or (spam_score >= 1 and link_count >= 1):
            raise forms.ValidationError(
                "A mensagem parece ser spam. Revise o conteúdo ou fale pelo WhatsApp."
            )

        return message

    def clean(self):
        cleaned_data = super().clean()

        if settings.RECAPTCHA_ENABLED and not self._recaptcha_is_valid():
            raise forms.ValidationError("Confirme que você não é um robô.")

        return cleaned_data

    def _recaptcha_is_valid(self):
        token = self.data.get("g-recaptcha-response", "")
        if not token:
            return False

        payload = parse.urlencode(
            {
                "secret": settings.RECAPTCHA_SECRET_KEY,
                "response": token,
                "remoteip": self.remote_ip or "",
            }
        ).encode()

        try:
            verify_request = request.Request(
                settings.RECAPTCHA_VERIFY_URL,
                data=payload,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            with request.urlopen(verify_request, timeout=5) as response:
                result = json.loads(response.read().decode("utf-8"))
        except (OSError, URLError, json.JSONDecodeError):
            return False

        return result.get("success") is True

    def save(self, commit=True):
        self.cleaned_data.pop("recaptcha_token", None)
        self.cleaned_data.pop("website", None)
        return super().save(commit=commit)
