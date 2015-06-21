from settings.settings import TEMPLATE_DIRS
from apps.generic.models import Produto
from django.shortcuts import render

from apps.generic.views import EphemeralTemplateView

class AccountCheckoutView(EphemeralTemplateView):
    template_name = "checkout.html"

    def get(self, request, **kwargs):
        return super(AccountCheckoutView, self).get(request, **kwargs)

    def post(self, request, **kwargs):
        return self.get(request, **kwargs)
