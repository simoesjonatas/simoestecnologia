from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contato", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contato",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="contato",
            name="organization",
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name="contato",
            name="solution_type",
            field=models.CharField(
                choices=[
                    ("sistema-personalizado", "Desenvolvimento de sistema personalizado"),
                    ("gestao-encomendas", "Gestão de encomendas"),
                    ("gestao-cobrancas", "Gestão de cobranças"),
                    ("fabriq", "Controle de fábrica - Fabriq"),
                    ("gestao-escalas", "Gestão de escalas"),
                    ("controle-entrada-saida", "Controle de entrada e saída"),
                    ("integracao-automacao", "Integração ou automação"),
                    ("consultoria-tecnica", "Consultoria técnica"),
                    ("outro", "Outro"),
                ],
                default="sistema-personalizado",
                max_length=60,
            ),
        ),
        migrations.AddField(
            model_name="contato",
            name="whatsapp",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
