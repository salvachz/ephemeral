from settings.settings import TEMPLATE_DIRS
from apps.generic.models import Produto
from django.shortcuts import render
from django.http import QueryDict

from apps.generic.views import EphemeralTemplateView

class WishlistView(EphemeralTemplateView):
    template_name = "wishlist.html"

    def get(self, request, **kwargs):
        if 'wishlist' not in request.session:
            request.session['wishlist'] = {}
        items = request.session['wishlist'].copy()
        kwargs['products'] = Produto.objects.filter(id__in=items.keys())
        kwargs['wishlist'] = items
        return super(WishlistView, self).get(request, **kwargs)

    def post(self, request, **kwargs):
        if 'wishlist' not in request.session:
            request.session['wishlist'] = {}
        product_id = str(request.POST.get('product',''))
        product_qnt = int(request.POST.get('qnt',1))
        if product_id and product_qnt:
            if product_id not in request.session['wishlist']:
                request.session['wishlist'][product_id] = product_qnt
            else:
                request.session['wishlist'][product_id] = int(request.session['wishlist'][product_id])+product_qnt
        request.session.modfied = True
        return self.get(request, **kwargs)

    def delete(self, request, **kwargs):
        if 'wishlist' not in request.session:
            request.session['wishlist'] = {}
        delete = QueryDict(request.body)
        product_id = str(delete.get('product',''))
        product_qnt = int(delete.get('qnt',1))
        if product_id and product_qnt:
            if product_id in request.session['wishlist']:
                del(request.session['wishlist'][product_id])
                request.session.modfied = True
        return self.get(request, **kwargs)
