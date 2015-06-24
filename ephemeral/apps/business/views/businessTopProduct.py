from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect
from apps.generic.models import Pedido, Produto, PedidoProduto

class BusinessTopProductView(EphemeralTemplateView):
    template_name = "business/businessTopProduct.html"

    def get(self, request, **kwargs):
        topProducts = []
        distinct_products = PedidoProduto.objects
        return EphemeralTemplateView.get(self, request,**kwargs)