import time

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .forms import ContatoForm
from simoes_tecnologia.views import build_page_context


def contato_view(request):
    if request.method == "POST":
        form = ContatoForm(request.POST, remote_ip=get_client_ip(request))
        last_submission = request.session.get("last_contact_submission", 0)
        is_repeated = time.time() - float(last_submission or 0) < 25

        if is_repeated:
            form.add_error(None, "Aguarde alguns segundos antes de enviar uma nova mensagem.")
        elif form.is_valid():
            form.save()
            request.session["last_contact_submission"] = time.time()
            messages.success(
                request,
                "Mensagem recebida. Entraremos em contato pelo canal informado.",
            )
            return redirect(f"{reverse('home')}#contato")

        return render(
            request,
            "home.html",
            build_page_context(request, form=form),
            status=400,
        )

    return redirect(f"{reverse('home')}#contato")


def get_client_ip(request):
    forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")
