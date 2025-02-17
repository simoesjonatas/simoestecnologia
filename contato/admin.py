from django.contrib import admin
from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # Campos para mostrar na listagem
    search_fields = ('name', 'email')  # Campos por onde a busca pode ser feita
    list_filter = ('email',)  # Filtros disponíveis na barra lateral
