import os
import requests
from django.core.management.base import BaseCommand

from apps.migration.utils import get_files_list, get_path_from_url

BASE_FOLDER = "_tmp"


class Command(BaseCommand):
    help = "Transfers media files from http source to http tarqet"

    def add_arguments(self, parser):
        parser.add_argument("source", type=str)
        parser.add_argument("target", type=str)

    def handle(self, *args, **options):
        files_list = get_files_list(options["source"])
        print(f"got list with {len(files_list)} elements")
        for file_url in files_list:
            current_file_path = get_path_from_url(file_url)
            print(f"current_file_path: {current_file_path}")
            save_path = os.path.join(
                os.path.dirname(__file__), BASE_FOLDER, current_file_path
            )
            print(f"check if {save_path} exists")
            if not os.path.exists(save_path):
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                response = requests.get(file_url, stream=True)
                if response.status_code == 200:
                    print(f"save {save_path}")
                    with open(save_path, "wb") as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
