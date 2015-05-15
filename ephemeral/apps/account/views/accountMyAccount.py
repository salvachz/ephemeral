from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect
from apps.account.forms import UserForm

class AccountMyAccountView(EphemeralTemplateView):
    template_name = "account/accountMyAccount.html"

    def get(self, request, **kwargs):
        kwargs['userForm'] = UserForm(instance=request.user)
        return EphemeralTemplateView.get(self, request, **kwargs)

    def post(self, request, **kwargs):
        userForm = kwargs['userForm'] = UserForm(request.POST, instance=request.user)
        if userForm.is_valid():
            kwargs['success'] = "Conta alterada com sucesso!"
            userForm.save()
        return EphemeralTemplateView.get(self, request, **kwargs)