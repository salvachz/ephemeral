from django.http import Http404,HttpResponse
from settings.settings import TEMPLATE_DIRS
from apps.generic.models import Produto
from django.shortcuts import render

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, *args, **kwargs):
	    try:
	        p = Produto.objects.all()
	    except :
	        raise Http404("Produto nao existe")
	    print kwargs
	    kwargs['features_items'] = p
	    return super(HomeView, self).get(*args, **kwargs)
	    # return HttpResponse(self.template_name)
	    # return render(self.template_name, {'features_items': p})