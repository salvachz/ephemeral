from settings.settings import TEMPLATE_DIRS
from apps.generic.models import Produto, Pedido,ProdutoPedido
from django.shortcuts import render
from django.db import transaction, IntegrityError
from django.http import HttpResponseRedirect

from apps.generic.views import EphemeralTemplateView

class AccountOrderDetailView(EphemeralTemplateView):
    template_name = "account/accountOrderDetail.html"

    def get(self, request, **kwargs):
        order_id = request.GET.get('id', None)
        if not order_id or not order_id.isdigit():
            return HttpResponseRedirect('/conta/meus-pedidos/')
        pdt = Pedido.objects.get(id=order_id)
        if pdt and pdt.usuario == request.user:
            kwargs['orders'] = ProdutoPedido.objects.filter(pedido=pdt)
        return EphemeralTemplateView.get(self, request, **kwargs)