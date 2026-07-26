import json

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render

from contato.forms import ContatoForm
from .content import SITE, SOLUTIONS, get_site_context, get_solution


def _canonical_url(request):
    return f"{SITE['domain'].rstrip('/')}{request.path}"


def _organization_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": SITE["name"],
        "url": SITE["domain"],
        "logo": f"{SITE['domain'].rstrip('/')}/static/images/simoeslogo2.png",
        "description": SITE["description"],
    }


def _software_schema(solution=None):
    source = [solution] if solution else SOLUTIONS
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "name": item["name"],
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "Web",
                "description": item["short_description"],
                "url": f"{SITE['domain'].rstrip('/')}/solucoes/{item['slug']}/",
                "publisher": {
                    "@type": "Organization",
                    "name": SITE["name"],
                    "url": SITE["domain"],
                },
            }
            for item in source
        ],
    }


def build_page_context(request, **extra):
    solution = extra.get("solution")
    context = get_site_context()
    context.update(
        {
            "canonical_url": _canonical_url(request),
            "page_title": extra.get("page_title") or SITE["title"],
            "page_description": extra.get("page_description") or SITE["description"],
            "og_image": f"{SITE['domain'].rstrip('/')}/static/images/simoeslogo2.png",
            "organization_schema": json.dumps(_organization_schema(), ensure_ascii=False),
            "software_schema": json.dumps(_software_schema(solution), ensure_ascii=False),
            "recaptcha_enabled": settings.RECAPTCHA_ENABLED,
            "recaptcha_site_key": settings.RECAPTCHA_SITE_KEY,
        }
    )
    context.update(extra)
    return context


def home(request):
    form = ContatoForm()
    return render(request, "home.html", build_page_context(request, form=form))


def solution_detail(request, slug):
    solution = get_solution(slug)
    if solution is None:
        raise Http404("Solução não encontrada")

    title = f"{solution['name']} | Soluções Simões Tecnologia"
    description = solution["short_description"]
    context = build_page_context(
        request,
        solution=solution,
        form=ContatoForm(initial={"solution_type": _initial_solution_type(slug)}),
        page_title=title,
        page_description=description,
    )
    return render(request, "solution_detail.html", context)


def privacy_policy(request):
    return render(
        request,
        "privacy_policy.html",
        build_page_context(
            request,
            page_title="Política de Privacidade | Simões Tecnologia",
            page_description="Informações sobre o tratamento de dados enviados à Simões Tecnologia.",
            form=ContatoForm(),
        ),
    )


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {SITE['domain'].rstrip('/')}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def sitemap_xml(request):
    urls = [
        {"loc": f"{SITE['domain'].rstrip('/')}/", "priority": "1.0"},
        {"loc": f"{SITE['domain'].rstrip('/')}/politica-de-privacidade/", "priority": "0.3"},
    ]
    urls.extend(
        {"loc": f"{SITE['domain'].rstrip('/')}/solucoes/{solution['slug']}/", "priority": "0.8"}
        for solution in SOLUTIONS
    )
    return render(
        request,
        "sitemap.xml",
        {"urls": urls},
        content_type="application/xml",
    )


def _initial_solution_type(slug):
    mapping = {
        "encomendas-condominio": "gestao-encomendas",
        "gestao-cobrancas": "gestao-cobrancas",
        "fabriq": "fabriq",
        "connect-pibvp": "gestao-escalas",
        "ebf-checkin": "controle-entrada-saida",
    }
    return mapping.get(slug, "sistema-personalizado")
