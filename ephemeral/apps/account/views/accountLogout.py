from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

class AccountLogoutView(EphemeralTemplateView):

    def get(self, request, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')
