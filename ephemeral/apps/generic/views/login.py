# -*- coding: utf-8 -*-
from apps.generic.forms.login import LoginForm
from django.contrib.auth import authenticate, login
from apps.generic.views import EphemeralTemplateView
from apps.generic.forms import RegistryForm

class LoginView(EphemeralTemplateView):
    template_name = "login.html"

    def get(self, request, **kwargs):
        kwargs['show_slider'] = False
        kwargs['show_recommended'] = False
        kwargs['registryForm'] = RegistryForm()
        kwargs['loginForm'] = LoginForm()
        return EphemeralTemplateView.get(self, request, **kwargs)

    def post(self, request, **kwargs):
        kwargs['registryForm'] = RegistryForm()
        kwargs['loginForm'] = LoginForm(request.POST)
        loginForm = kwargs['loginForm']
        if kwargs['loginForm'].is_valid():
            user = authenticate(email=loginForm.cleaned_data['email'], password=loginForm.cleaned_data['password'])
            if user:
                print 'tem user'
                if user.is_active:
                    print 'foi'
                    login(request, user)
        return EphemeralTemplateView.get(self, request, **kwargs)



# class AuthView(views.APIView):
#     def post(self, request, format=None):
#         data = json.loads(request.body)

#         email = data.get('email', None)
#         password = data.get('password', None)

#         user = authenticate(email=email, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
