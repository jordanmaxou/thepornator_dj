from django.views.generic.base import TemplateView


class StoryListView(TemplateView):
    template_name = "stories/list.html"


class StoryDetailView(TemplateView):
    template_name = "stories/detail.html"
