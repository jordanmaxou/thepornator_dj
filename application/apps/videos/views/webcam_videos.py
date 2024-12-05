import requests

from django.http import Http404
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse


from libs.request import get_client_ip


class WebcamVideosIndexListView(TemplateView):
    template_name = "videos/webcamvideos/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": _("Webcam Porn videos"),
            },
        ]
        context["head"] = {
            "title": _(
                "Free Live Sex Webcam porn videos - Hot XXX Camgirls - The Pornator"
            ),
            "description": _(
                "Discover the finest collection of complimentary XXX webcam videos available on thepornator.com. Have a preferred live cam model you'd like to see undressed? Explore them all right here."
            ),
        }
        response = requests.get(
            settings.VIDEOS_WEBCAM_URL + f"&clientIp={get_client_ip(self.request)}"
        )
        if response.ok and (data := response.json()) and data.get("success") is True:
            context["videos"] = data.get("data", {}).get("videos")
        else:
            raise Http404("A problem occured during webcam videos retrieval")
        return context


@method_decorator(xframe_options_exempt, name="dispatch")
class WebcamVideosContentListView(TemplateView):
    template_name = "videos/webcamvideos/content.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = settings.VIDEO_WEBCAM_DETAIL.format(
            video_id=self.kwargs.get("slug"), client_ip=get_client_ip(self.request)
        )

        response = requests.get(url)
        if response.ok and (data := response.json()) and data.get("success") is True:
            video = data.get("data")
            context["breadcrumbs"] = [
                {
                    "label": _("Webcam Porn videos"),
                    "link": reverse("videos:webcam-videos-index"),
                },
                {
                    "label": video["title"][:20] + "..."
                    if len(video["title"]) > 20
                    else ""
                },
            ]
            context["video"] = {
                **video,
                "url": f"//wmcdpt.com/tube-player/?psid=thepornator&pstool=421_3&accessKey=335d14527f9a29381e1c0405caca83d4&campaign_id=&site=jsm&psprogram=VPAPI&contentHash={self.kwargs.get('slug')}&primaryColor=8AC437&labelColor=212121&c=videoplayer&disableOverlayClick=0&embedTool=1&origin=",
            }

            context["head"] = {
                "title": _("%(model)s in free webcam porn video - Thepornator")
                % {"model": video["performerId"]},
                "description": _(
                    "%(model)s %(title)s - Watch free webcam porn video - Thepornator"
                )
                % {"model": video["performerId"], "title": video["title"]},
            }
        else:
            raise Http404("A problem occured during webcam videos retrieval")
        return context
