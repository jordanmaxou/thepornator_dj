from urllib.parse import urlparse
from os.path import basename, splitext


def extract_code_from_url(url: str) -> str:
    code, _ = splitext(basename(urlparse(url).path))
    return code
