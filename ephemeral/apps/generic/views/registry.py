from apps.generic.views import EphemeralTemplateView
from apps.generic.forms import RegistryForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

class RegistryView(EphemeralTemplateView):
    template_name = "registry.html"

    def get(self, request, **kwargs):
        kwargs['registryForm'] = RegistryForm()
        return EphemeralTemplateView.get(self, request, **kwargs)

    def post(self, request, **kwargs):
        kwargs['registryForm'] = RegistryForm(request.POST)
        if kwargs['registryForm'].is_valid():
            kwargs['registryForm'].save()
            return render(request, 'thanks.html')
        return EphemeralTemplateView.get(self, request, **kwargs)

