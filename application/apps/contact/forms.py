from django import forms
from django.utils.translation import gettext_lazy as _

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": _("Your name")}
        ),
    )
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": _("Your name")}
        ),
    )
    subject = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": _("Subject")}
        ),
    )
    message = forms.CharField(
        max_length=10000,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": _("Your message")}
        ),
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
