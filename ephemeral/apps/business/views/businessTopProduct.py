from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect
from django.db.models import Sum
from apps.generic.models import Pedido, Produto, ProdutoPedido

class BusinessTopProductView(EphemeralTemplateView):
    template_name = "business/businessTopProduct.html"

    def get(self, request, **kwargs):
        kwargs['topProducts'] = []
        products = ProdutoPedido.objects.values('produto_id').distinct()
        for product_row in products:
            data = {}
            product_id = product_row['produto_id']
            data['product'] = Produto.objects.get(id=product_id)
            data['orders'] = ProdutoPedido.objects.filter(produto_id=product_id).count()
            data['sumQnt'] = "%.2f" % (ProdutoPedido.objects.filter(produto_id=product_id).aggregate(Sum('quantidade'))['quantidade__sum']/float(data['orders']))
            kwargs['topProducts'].append(data)
        return EphemeralTemplateView.get(self, request,**kwargs)