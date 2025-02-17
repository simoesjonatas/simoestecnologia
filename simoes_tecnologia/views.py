from django.shortcuts import render
from contato.forms import ContatoForm

def home(request):
    form = ContatoForm()
    return render(request, 'home.html', {'form': form})
