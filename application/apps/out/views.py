import json

from django.views.generic.base import View
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse

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
        elif type_out == "website":
            website = get_object_or_404(Website, id=id)
            website.update_counter()

            return redirect(website.url, permanent=True)
        raise Http404("No redirect found")


class VideoVoteUpdate(View):
    def post(self, request, id):
        data = json.loads(request.body)
        video = get_object_or_404(Video, id=id)
        if (type_vote := data.get("type")) and (type_vote in ["up", "down"]):
            if type_vote == "up":
                video.vote_up()
            else:
                video.vote_down()
            return HttpResponse(status=201)
        return HttpResponse(status=400)
