from django.contrib import admin
from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "email", "whatsapp", "solution_type", "created_at")
    search_fields = ("name", "organization", "email", "whatsapp", "message")
    list_filter = ("solution_type", "created_at")
    readonly_fields = ("created_at",)
