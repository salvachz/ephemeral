# -*- coding: utf-8 -*-
from apps.generic.forms.login import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from apps.generic.views import EphemeralTemplateView
from apps.generic.forms import RegistryForm

class LoginView(EphemeralTemplateView):
    template_name = "login.html"

    def get(self, request, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/conta/')
        kwargs['show_slider'] = False
        kwargs['show_recommended'] = False
        kwargs['registryForm'] = RegistryForm()
        kwargs['loginForm'] = LoginForm()
        return EphemeralTemplateView.get(self, request, **kwargs)

    def post(self, request, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/conta/')
        kwargs['registryForm'] = RegistryForm()
        kwargs['loginForm'] = LoginForm(request.POST)
        loginForm = kwargs['loginForm']
        if kwargs['loginForm'].is_valid():
            user = authenticate(email=loginForm.cleaned_data['email'], password=loginForm.cleaned_data['password'])
            if user and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/conta/')
        return EphemeralTemplateView.get(self, request, **kwargs)