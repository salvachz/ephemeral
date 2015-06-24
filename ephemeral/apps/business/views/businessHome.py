from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect

class BusinessHomeView(EphemeralTemplateView):
    template_name = "business/businessHome.html"

    def get(self, request, **kwargs):
        return HttpResponseRedirect('/business/dashboard/')