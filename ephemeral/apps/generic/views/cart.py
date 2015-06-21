from settings.settings import TEMPLATE_DIRS
from apps.generic.models import Produto
from django.shortcuts import render

from apps.generic.views import EphemeralTemplateView

class CartView(EphemeralTemplateView):
    template_name = "cart.html"

    def get(self, request, **kwargs):
        if 'cart' not in request.session:
            request.session['cart'] = {}
        items = request.session['cart']
        kwargs['products'] = Produto.objects.filter(id__in=items.keys())
        kwargs['cart'] = items
        return super(CartView, self).get(request, **kwargs)

    def post(self, request, **kwargs):
        if 'cart' not in request.session:
            request.session['cart'] = {}
        product_id = str(request.POST.get('product',''))
        product_qnt = int(request.POST.get('qnt',1))
        if product_id and product_qnt:
            if product_id not in request.session['cart']:
                request.session['cart'][product_id] = product_qnt
            else:
                request.session['cart'][product_id] = int(request.session['cart'][product_id])+product_qnt
        request.session.modfied = True
        return self.get(request, **kwargs)