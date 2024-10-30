from django.views.generic.base import TemplateView


class BlogListView(TemplateView):
    template_name = "blog/list.html"


class BlogDetailView(TemplateView):
    template_name = "blog/detail.html"
