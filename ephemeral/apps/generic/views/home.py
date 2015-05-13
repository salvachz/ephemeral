from apps.generic.views import EphemeralTemplateView

class HomeView(EphemeralTemplateView):
    template_name = "home.html"

    def get(self, request, **kwargs):
        kwargs['filtro'] = self.get_filter(request)
        if kwargs['filtro']:
            kwargs['show_slider'] = False
            kwargs['show_recommended'] = False
        return EphemeralTemplateView.get(self, request, **kwargs)

