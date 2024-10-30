from django.views.generic.base import TemplateView
from django.utils.translation import gettext as _


class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sentence"] = _("Bienvenue sur mon site.")

        return context
