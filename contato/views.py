from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm

def contato_view(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Valeu! Sua mensagem foi enviada com sucesso. Entraremos em contato em breve!')
            return redirect('home')
    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form': form})

