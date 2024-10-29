from typing import Dict
import json

from django.conf import settings
from django.contrib.staticfiles.storage import StaticFilesStorage
from django.core.exceptions import ImproperlyConfigured
from django.core.cache import cache

import requests


class CustomStaticFilesStorage(StaticFilesStorage):
    MANIFEST_KEY = "static_manifest"

    def __init__(self, *args, **kwargs):
        manifest_url = kwargs.pop("manifest_url")
        super().__init__(*args, **kwargs)
        print(kwargs)
        self.options = kwargs.pop("options", {})
        self.manifest_url = manifest_url
        self.manifest = self._load_manifest()

    def _load_manifest(self) -> Dict[str, str]:
        manifest = cache.get(self.MANIFEST_KEY)
        if manifest is None:
            try:
                # FIXME: https://requests.readthedocs.io/en/latest/user/advanced/#client-side-certificates
                response = requests.get(self.manifest_url, verify=(not settings.DEBUG))
                response.raise_for_status()
                manifest = response.json()
                cache.set(self.MANIFEST_KEY, manifest, None)
            except requests.RequestException as e:
                raise ImproperlyConfigured(
                    f"Error fetching manifest from {self.manifest_url}: {e}"
                )
            except json.JSONDecodeError:
                raise ImproperlyConfigured(
                    f"Manifest fetched from {self.manifest_url} is not valid JSON"
                )
        return manifest

    def url(self, name) -> str:
        if name in self.manifest:
            name = self.manifest[name]
        return super().url(name)
