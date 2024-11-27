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
        return context

    def get_queryset(self):
        return super().get_queryset().filter(publication_date__lte=date.today())
