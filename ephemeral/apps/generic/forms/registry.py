# -*- coding: utf-8 -*-
from django import forms
from apps.generic.models import Usuario

default_error_message = {
    'required': 'Este campo é obrigatorio',
    'invalid': 'Valor invalido'
}

class RegistryForm(forms.ModelForm):
    # name = forms.CharField(label='Nome', max_length=100,error_messages=my_default_errors)
    # email = forms.CharField(label='Email',error_messages=my_default_errors)
    # password = forms.CharField(widget=forms.PasswordInput(),error_messages=my_default_errors)
    class Meta:
        model = Usuario
        exclude = ('status','is_admin','last_access_ip','last_login')
        widgets = {
            'password': forms.PasswordInput(),
        }
        error_messages = {
            'password':default_error_message,
            'nome':default_error_message,
            'email':default_error_message,
        }