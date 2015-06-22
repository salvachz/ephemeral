from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.http import urlquote


import re

class RequireLoginMiddleware(object):
    def __init__(self):
        self.urls = tuple([re.compile(url) for url in settings.LOGIN_REQUIRED_URLS])
        self.require_login_path = getattr(settings, 'LOGIN_URL', '/login/')
    
    def process_request(self, request, format=None):
        for url in self.urls:
            if url.match(request.path) and request.user.is_anonymous():
                print urlquote(request.path)
                return HttpResponseRedirect(
                    "%s?togo=%s" % (settings.LOGIN_URL, urlquote(request.path))
                )