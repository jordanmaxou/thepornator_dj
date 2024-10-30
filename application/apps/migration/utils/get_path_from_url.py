from urllib.parse import urlparse


def get_path_from_url(url: str) -> str:
    return urlparse(url).path.strip("/")
