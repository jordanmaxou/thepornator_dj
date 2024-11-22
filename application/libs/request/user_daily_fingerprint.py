import hashlib
from datetime import date

from .get_client_ip import get_client_ip


def user_daily_fingerprint(request):
    today = date.today().isoformat()
    user_agent = request.META.get("HTTP_USER_AGENT", "")
    ip_address = get_client_ip(request)
    data = f"{user_agent}-{ip_address}-{today}"

    return hashlib.sha256(data.encode("utf-8")).hexdigest()
