from apps.generic.views import EphemeralTemplateView

class ProductListView(EphemeralTemplateView):
    template_name = "product-list.html"

    def get(self, request, **kwargs):
        kwargs['filtro'] = self.get_filter(request)
        if kwargs['filtro']:
            kwargs['show_slider'] = False
            kwargs['show_recommended'] = False
        return EphemeralTemplateView.get(self, request, **kwargs)

