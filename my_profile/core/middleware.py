"""
Middleware that records a PageView entry for every public (non-admin) GET request.
Runs after the response is ready so it never slows down the user-facing response.
"""
import hashlib

from .models import PageView


def _device(ua: str) -> str:
    ua = ua.lower()
    if any(k in ua for k in ("ipad", "tablet", "kindle")):
        return "tablet"
    if any(k in ua for k in ("mobile", "android", "iphone", "ipod", "windows phone")):
        return "mobile"
    return "desktop"


class PageViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Only track public GET requests (skip admin, static, media, bots)
        path = request.path
        if (
            request.method == "GET"
            and not path.startswith("/admin")
            and not path.startswith("/static")
            and not path.startswith("/media")
            and response.status_code < 400
        ):
            ua = request.META.get("HTTP_USER_AGENT", "")
            # Skip obvious bots
            if not any(b in ua.lower() for b in ("bot", "crawl", "spider", "slurp", "wget", "curl")):
                ip = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR", ""))
                ip = ip.split(",")[0].strip()
                ip_hash = hashlib.sha256(ip.encode()).hexdigest()[:32] if ip else ""
                PageView.objects.create(
                    path=path,
                    referrer=request.META.get("HTTP_REFERER", "")[:500],
                    device=_device(ua),
                    ip_hash=ip_hash,
                )
        return response
