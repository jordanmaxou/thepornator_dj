from django.views.generic.base import View
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from apps.porn_models.models import Profile
from apps.videos.models import Video
from apps.websites.models import Website


class Out(View):
    def get(self, _request, type_out, id):
        if type_out == "model":
            profile = get_object_or_404(Profile, id=id)
            profile.update_counter()

            return redirect(profile.url, permanent=True)
        elif type_out == "video":
            video = get_object_or_404(Video, id=id)
            video.update_counter()

            return redirect(video.link, permanent=True)

        raise Http404("No redirect found")


class OutWebsite(View):
    def get(self, _request, site_slug):
        website = get_object_or_404(Website, slug=site_slug)
        website.update_counter()

        return redirect(website.url, permanent=True)
