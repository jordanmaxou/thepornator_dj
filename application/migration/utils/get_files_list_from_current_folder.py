from typing import List
import requests

from .get_url import get_url


def get_files_list_from_current_folder(url: str) -> List[str]:
    response = requests.get(url)
    content = response.content.decode()

    return [
        result
        for row in content.split("\n")
        if (
            (strip_row := row.strip())
            and strip_row.startswith("<img")
            and (result := get_url(strip_row))
        )
    ]
