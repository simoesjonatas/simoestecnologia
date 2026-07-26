from django.db import models

from simoes_tecnologia.content import CONTACT_SOLUTION_CHOICES


class Contato(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=160, blank=True)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=30, blank=True)
    solution_type = models.CharField(
        max_length=60,
        choices=CONTACT_SOLUTION_CHOICES,
        default="sistema-personalizado",
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
