from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect

class BusinessDashboardView(EphemeralTemplateView):
    template_name = "business/businessDashboard.html"

    def get(self, request, **kwargs):
        return EphemeralTemplateView.get(self, request,**kwargs)