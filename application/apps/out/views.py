from django.views.generic.base import View
from django.shortcuts import redirect, get_object_or_404
from apps.porn_models.models import Profile
from apps.videos.models import Video


class Out(View):
    def get(self, request, type_out, id):
        if type_out == "model":
            profile = get_object_or_404(Profile, id=id)
            # TODO: increment counts
            return redirect(profile.url)
        elif type_out == "video":
            video = get_object_or_404(Video, id=id)
            return redirect(video.link)
