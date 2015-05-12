from settings.settings import TEMPLATE_DIRS
from apps.generic.models import Produto
from django.shortcuts import render

from apps.generic.views import EphemeralTemplateView

class ProductDetailView(EphemeralTemplateView):
    template_name = "product-detail.html"

    def get(self, *args, **kwargs):
        print args, kwargs
        try:
            slug = kwargs['slug']
            kwargs['produto'] = Produto.objects.get(slug=slug)
        except:
        	return render(args[0],template_name='404.html',status=404)
        return super(ProductDetailView, self).get(*args, **kwargs)
