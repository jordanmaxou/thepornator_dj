from typing import Optional
from os.path import join
from urllib.parse import unquote, quote
from re import search


def get_url(row: str, prefix: str = "") -> Optional[str]:
    match = search(r"<a href=\"([^\"]+)\"", row)
    if match:
        return join(prefix, quote(unquote(match.group(1))))
    return None
