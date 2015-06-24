from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect

class AccountHomeView(EphemeralTemplateView):
    template_name = "account/accountHome.html"

    def get(self, request, **kwargs):
        return HttpResponseRedirect('/conta/minha-conta/')