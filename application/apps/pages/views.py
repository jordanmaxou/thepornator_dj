from django.views.generic.base import TemplateView


class ContactView(TemplateView):
    template_name = "pages/contact.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"
