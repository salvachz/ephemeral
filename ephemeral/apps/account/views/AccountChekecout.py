from settings.settings import TEMPLATE_DIRS
from apps.generic.models import Produto, Pedido,ProdutoPedido
from django.shortcuts import render
from apps.business.models import Compra
from django.db import transaction, IntegrityError
from datetime import datetime

from apps.generic.views import EphemeralTemplateView

class AccountCheckoutView(EphemeralTemplateView):
    template_name = "checkout.html"

    def get(self, request, **kwargs):
        if 'cart' in request.session:
            items = request.session['cart']
            kwargs['products'] = Produto.objects.filter(id__in=items.keys())
            kwargs['cart'] = items
        return EphemeralTemplateView.get(self, request, **kwargs)

    def post(self, request, **kwargs):
        if 'cart' not in request.session:
            return self.get(request, **kwargs)
        self.__add_buy(request)
        forma_pagamento = request.POST.get('pagform','boleto')
        try:
            with transaction.atomic():
                pedido = Pedido(usuario=request.user,forma_pagamento=forma_pagamento)
                pedido.save()
                for product_id, qnt in request.session['cart'].items():
                    pdt = Produto.objects.get(id=product_id)
                    if pdt.quantidade < qnt:
                        raise IntegrityError("Produto %s indisponivel nessa quantidade." % pdt.nome)
                    pdt.quantidade = pdt.quantidade - qnt
                    ProdutoPedido(pedido=pedido, produto=pdt,quantidade=qnt).save()
                    pdt.save()
                request.session['cart'] = {}
        except IntegrityError as e:
            print 'ERROR ON PEDIDO',e
            erroMessage = e
        return self.get(request, **kwargs)

    def __add_buy(self, request):
            compra = Compra()
            compra.usuario = request.user
            compra.data = datetime.now()
            compra.save()
