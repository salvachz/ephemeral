from apps.generic.models import Produto, Categoria, Marca

from django.views.generic import TemplateView
from apps.business.models import Visita
from datetime import datetime

class EphemeralTemplateView(TemplateView):

    def get(self, request, **kwargs):
        visita = Visita()
        visita.usuario = request.user if not request.user.is_anonymous() else None
        visita.data = datetime.now()
        visita.save()
        kwargs['filtro'] = kwargs.get('filtro',{})
        kwargs['features_items'] = Produto.objects.filter(**kwargs['filtro'])
        search = request.GET.get('search','')
        if search:
            kwargs['features_items'] = kwargs['features_items'].filter(nome__icontains=search)
            kwargs['search'] = search
        kwargs['categorys'] = Categoria.get_quantified()
        kwargs['brands'] = Marca.get_quantified()
        kwargs['show_slider'] = kwargs.get('show_slider',True)
        kwargs['show_recommended'] = kwargs.get('show_recommended',True)
        kwargs['recommended_items'] = [Produto.objects.all()] + [Produto.objects.all()]
        return super(EphemeralTemplateView, self).get(request, **kwargs)

    def get_filter(self, request):
        categoria = request.GET.get('categoria','')
        marca = request.GET.get('marca','')

        categoria = Categoria.objects.get(id=categoria) if categoria.isdigit() else None
        marca = Marca.objects.get(id=marca) if marca.isdigit() else None
        retorno = {}
        if categoria:
            retorno['categoria'] = categoria
        if marca:
            retorno['marca']= marca
        return retorno
