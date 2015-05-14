from apps.generic.views import EphemeralTemplateView
from apps.generic.forms import RegistryForm

class LoginView(EphemeralTemplateView):
    template_name = "login.html"

    def get(self, request, **kwargs):
        kwargs['show_slider'] = False
        kwargs['show_recommended'] = False
        kwargs['registryForm'] = RegistryForm()
        return EphemeralTemplateView.get(self, request, **kwargs)

