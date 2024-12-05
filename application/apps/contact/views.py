from django.shortcuts import render
from django.utils.translation import gettext as _

from apps.contact.forms import ContactForm
from apps.contact.models import Message


def contact(request):
    context = {}
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            Message.objects.create(
                name=data["name"],
                email=data["email"],
                subject=data["subject"],
                message=data["message"],
            )
            context["message_success"] = _(
                'Your message has been sent. If you have no response, please send an email directly to <a href="mailto:contact@thepornator.com">contact@thepornator.com</a>'
            )
        else:
            if (
                form.errors
                and (errors := form.errors.as_data())
                and ("captcha" in errors.keys())
            ):
                context["message_error"] = _(
                    "Please proceed captcha according to check if you're not a bot."
                )
            else:
                context["message_error"] = _(
                    'A problem occurs during message sending. Please send an email directly to <a href="mailto:contact@thepornator.com">contact@thepornator.com</a>'
                )

    context["breadcrumbs"] = [
        {
            "label": _("Contact"),
        },
    ]
    context["head"] = {
        "title": _("Contact the Pornator"),
        "description": _(
            "If you want to be listed on this porn directory, fill the form and I will reach out to you quickly"
        ),
    }
    context["form"] = ContactForm()
    return render(request, "contact/contact.html", context)
