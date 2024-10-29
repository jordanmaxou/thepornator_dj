from urllib.parse import urljoin
from typing import List

from .get_files_list_from_current_folder import get_files_list_from_current_folder
from .is_folder import is_folder


def get_files_list(base_url: str, files_list: List[str] = []) -> List[str]:
    current_paths = get_files_list_from_current_folder(base_url)
    for current_path in current_paths:
        if is_folder(current_path):
            get_files_list(urljoin(base_url, current_path), files_list)
        else:
            files_list.append(urljoin(base_url, current_path))
    return files_list
