from settings.settings import TEMPLATE_DIRS
from apps.generic.models import Produto
from django.shortcuts import render
from django.http import QueryDict

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
            if request.POST.get('from','') == 'wishlist':
                if product_id in request.session['wishlist']:
                    del(request.session['wishlist'][product_id])
            if product_id not in request.session['cart']:
                request.session['cart'][product_id] = product_qnt
            else:
                request.session['cart'][product_id] = int(request.session['cart'][product_id])+product_qnt
        request.session.modfied = True
        return self.get(request, **kwargs)

    def delete(self, request, **kwargs):
        if 'cart' not in request.session:
            request.session['cart'] = {}
        delete = QueryDict(request.body)
        product_id = str(delete.get('product',''))
        product_qnt = int(delete.get('qnt',1))
        if product_id and product_qnt:
            if product_id in request.session['cart']:
                del(request.session['cart'][product_id])
                request.session.modfied = True
        return self.get(request, **kwargs)

    def put(self, request, **kwargs):
        if 'cart' not in request.session:
            request.session['cart'] = {}
        update = QueryDict(request.body)
        print 'update valendo',update
        product_id = str(update.get('product',''))
        product_qnt = int(update.get('qnt',1))
        if product_id and product_qnt:
            print 'era',request.session['cart'][product_id]
            request.session['cart'][product_id] = product_qnt
            print 'ficou',request.session['cart'][product_id]
        request.session.modfied = True
        return self.get(request, **kwargs)