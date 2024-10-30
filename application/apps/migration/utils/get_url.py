from typing import Optional
from os.path import join
from re import search


def get_url(row: str, prefix: str = "") -> Optional[str]:
    match = search(r"<a href=\"([^\"]+)\"", row)
    if match:
        return join(prefix, match.group(1))
    return None
