from apps.generic.models import Produto, Categoria, Marca

from django.views.generic import TemplateView

class EphemeralTemplateView(TemplateView):

    def get(self, *args, **kwargs):
	    kwargs['features_items'] = Produto.objects.all()
	    kwargs['categorys'] = Categoria.objects.all()
	    kwargs['brands'] = Marca.objects.all()
	    kwargs['recommended_items'] = [Produto.objects.all()] + [Produto.objects.all()]
	    return super(EphemeralTemplateView, self).get(*args, **kwargs)
