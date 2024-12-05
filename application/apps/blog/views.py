from datetime import date

from django.views.generic import ListView, DetailView
from django.utils.translation import gettext as _
from django.urls import reverse

from apps.blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog/list.html"
    context_object_name = "blogs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Blog"),
            },
        ]
        context["head"] = {
            "title": _(
                "Porn Blog - All the things you have to know about porn - The Pornator"
            ),
            "description": _(
                "Read about the latest porn news, special XXX topics or porn stars. A no-holds-barred space of freedom on the porn scene!"
            ),
        }
        return context

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(publication_date__lte=date.today())
            .order_by("-publication_date")
        )


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"label": _("Blog"), "link": reverse("blog:index")},
            {"label": self.object.title},
        ]
        context["head"] = {
            "title": _("%(title)s - Blog - The Pornator")
            % {"title": self.object.title},
            "description": f"{self.object.content[:140]}{'...' if len(self.object.content) > 140 else ''}",
        }
        return context

    def get_queryset(self):
        return super().get_queryset().filter(publication_date__lte=date.today())
