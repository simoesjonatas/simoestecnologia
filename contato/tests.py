from django.test import TestCase, override_settings
from django.urls import reverse

from simoes_tecnologia.content import SOLUTIONS
from .models import Contato


class InstitucionalSiteTests(TestCase):
    def test_home_renders_new_institutional_content(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tecnologia que transforma processos em resultados")
        self.assertContains(response, "Soluções que já desenvolvemos")
        self.assertContains(response, "Da necessidade à solução")

    def test_solution_pages_render_from_centralized_data(self):
        for solution in SOLUTIONS:
            with self.subTest(solution=solution["slug"]):
                response = self.client.get(
                    reverse("solution_detail", kwargs={"slug": solution["slug"]})
                )

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, solution["name"])
                self.assertContains(response, solution["short_description"])

    def test_contact_form_saves_new_fields(self):
        response = self.client.post(
            reverse("contato"),
            data={
                "name": "Cliente Teste",
                "organization": "Empresa Teste",
                "email": "cliente@example.com",
                "whatsapp": "(11) 99999-9999",
                "solution_type": "fabriq",
                "message": "Quero organizar um processo produtivo.",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/#contato")
        self.assertEqual(Contato.objects.count(), 1)
        contato = Contato.objects.get()
        self.assertEqual(contato.organization, "Empresa Teste")
        self.assertEqual(contato.solution_type, "fabriq")

    def test_contact_form_rejects_invalid_email(self):
        response = self.client.post(
            reverse("contato"),
            data={
                "name": "Cliente Teste",
                "organization": "Empresa Teste",
                "email": "email-invalido",
                "whatsapp": "(11) 99999-9999",
                "solution_type": "gestao-cobrancas",
                "message": "Preciso centralizar cobranças.",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Contato.objects.count(), 0)
        self.assertContains(response, "Informe um e-mail válido.", status_code=400)

    def test_contact_form_rejects_crypto_spam_pattern(self):
        response = self.client.post(
            reverse("contato"),
            data={
                "name": "LarryBuics",
                "organization": "LarryBuics",
                "email": "tracey37usmc@live.com",
                "whatsapp": "85821519882",
                "solution_type": "gestao-cobrancas",
                "message": (
                    "Earn $1,500 per day or more by reviewing crypto projects "
                    "https://telegra.ph/Collect-cryptocurrency-automatically-every-day"
                ),
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Contato.objects.count(), 0)
        self.assertContains(response, "A mensagem parece ser spam.", status_code=400)

    @override_settings(
        RECAPTCHA_ENABLED=True,
        RECAPTCHA_SITE_KEY="site-key-test",
        RECAPTCHA_SECRET_KEY="secret-key-test",
    )
    def test_contact_form_requires_recaptcha_when_enabled(self):
        response = self.client.post(
            reverse("contato"),
            data={
                "name": "Cliente Teste",
                "organization": "Empresa Teste",
                "email": "cliente@example.com",
                "whatsapp": "(11) 99999-9999",
                "solution_type": "fabriq",
                "message": "Quero organizar um processo produtivo.",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Contato.objects.count(), 0)
        self.assertContains(response, "Confirme que você não é um robô.", status_code=400)
        self.assertContains(response, "data-captcha-field", status_code=400)

    def test_seo_support_routes(self):
        robots = self.client.get(reverse("robots_txt"))
        sitemap = self.client.get(reverse("sitemap_xml"))

        self.assertEqual(robots.status_code, 200)
        self.assertContains(robots, "Sitemap: https://simoesti.com.br/sitemap.xml")
        self.assertEqual(sitemap.status_code, 200)
        self.assertContains(sitemap, "https://simoesti.com.br/solucoes/fabriq/")
