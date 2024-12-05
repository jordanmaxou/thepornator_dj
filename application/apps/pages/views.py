from django.views.generic.base import TemplateView
from django.utils.translation import gettext as _
from django.shortcuts import render

from apps.trends.models import TrendingSearches


class AboutView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("About the Pornator"),
            },
        ]
        context["head"] = {
            "title": _("How do I contact you? how can I add my site?"),
            "description": _(
                "If you think that any awesome XXX sites are missing in my porn directory, I can be reached by email at first."
            ),
        }
        return context


class AdvertisingView(TemplateView):
    template_name = "pages/advertising.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Advertising"),
            },
        ]
        context["head"] = {
            "title": _("Advertising on Thepornator. Looking for qualified trafic?"),
            "description": _(
                "IDiscover all the advertising opportunities on thepornator.com. We offer a range of advertising spaces to enhance your site and bring you quality traffic."
            ),
        }
        return context


def custom_404_view(request, exception):
    return render(
        request,
        "404.html",
        {
            "trends": TrendingSearches.objects.top_15(),
            "head": {"title": _("Unknown page")},
        },
        status=404,
    )
