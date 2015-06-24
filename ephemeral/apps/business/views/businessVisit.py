from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect

class BusinessVisitView(EphemeralTemplateView):
    template_name = "business/businessVisit.html"

    def get(self, request, **kwargs):
        return EphemeralTemplateView.get(self, request,**kwargs)