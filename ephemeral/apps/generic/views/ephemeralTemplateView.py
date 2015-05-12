from apps.generic.models import Produto, Categoria, Marca

from django.views.generic import TemplateView

class EphemeralTemplateView(TemplateView):

    def get(self, *args, **kwargs):
	    kwargs['features_items'] = Produto.objects.all()
	    kwargs['categorys'] = Categoria.get_quantified()
	    kwargs['brands'] = Marca.get_quantified()
	    kwargs['recommended_items'] = [Produto.objects.all()] + [Produto.objects.all()]
	    return super(EphemeralTemplateView, self).get(*args, **kwargs)
