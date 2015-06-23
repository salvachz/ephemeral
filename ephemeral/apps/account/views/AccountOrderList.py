from settings.settings import TEMPLATE_DIRS
from apps.generic.models import Produto, Pedido,ProdutoPedido
from django.shortcuts import render
from django.db import transaction, IntegrityError

from apps.generic.views import EphemeralTemplateView

class AccountOrderListView(EphemeralTemplateView):
    template_name = "account/accountOrderList.html"

    def get(self, request, **kwargs):
        kwargs['orders'] = Pedido.objects.filter(usuario=request.user)
        return EphemeralTemplateView.get(self, request, **kwargs)