from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect

class BusinessCartConversionView(EphemeralTemplateView):
    template_name = "business/businessCartConversion.html"

    def get(self, request, **kwargs):
        return EphemeralTemplateView.get(self, request,**kwargs)