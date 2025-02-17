from django.shortcuts import render, redirect
from .forms import ContatoForm

def contato_view(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para uma URL de sucesso, por exemplo
    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form': form})
