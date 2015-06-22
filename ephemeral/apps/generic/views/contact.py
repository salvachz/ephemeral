from apps.generic.views import EphemeralTemplateView

class ContactView(EphemeralTemplateView):
    template_name = "contact.html"

    def get(self, request, **kwargs):
        return EphemeralTemplateView.get(self, request, **kwargs)

