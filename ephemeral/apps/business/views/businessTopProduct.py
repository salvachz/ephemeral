from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect
from apps.generic.models import Pedido, Produto, ProdutoPedido

class BusinessTopProductView(EphemeralTemplateView):
    template_name = "business/businessTopProduct.html"

    def get(self, request, **kwargs):
        topProducts = []
        
        return EphemeralTemplateView.get(self, request,**kwargs)