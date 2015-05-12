from django.http import Http404,HttpResponse
from settings.settings import TEMPLATE_DIRS
from apps.generic.models import Produto, Categoria, Marca
from django.shortcuts import render

from apps.generic.views import EphemeralTemplateView

class ProductDetailView(EphemeralTemplateView):
    template_name = "product-detail.html"

    def get(self, *args, **kwargs):
	    return super(ProductDetailView, self).get(*args, **kwargs)
