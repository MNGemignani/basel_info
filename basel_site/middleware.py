import re
from urllib.parse import urlencode, urlparse
from django.conf import settings
from django.shortcuts import redirect, resolve_url

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        login_url = resolve_url(settings.LOGIN_URL)
        self.login_path = urlparse(login_url).path.lstrip('/')

        self.exempt_patterns = [
            re.compile(rf'^{re.escape(self.login_path)}$'),
            re.compile(r'^accounts/logout/?$'),
            re.compile(r'^admin/'),
            re.compile(r'^static/'),
        ]

    def __call__(self, request):
        path = request.path_info.lstrip('/')

        if request.user.is_authenticated or any(p.match(path) for p in self.exempt_patterns):
            return self.get_response(request)

        login_url = resolve_url(settings.LOGIN_URL)
        q = request.GET.copy()
        if 'next' not in q:
            q['next'] = request.get_full_path()
        return redirect(f"{login_url}?{urlencode(q, doseq=True)}")
