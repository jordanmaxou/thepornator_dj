from django.views.generic.base import TemplateView


class StoryListView(TemplateView):
    template_name = "storys/list.html"


class StoryDetailView(TemplateView):
    template_name = "storys/detail.html"
