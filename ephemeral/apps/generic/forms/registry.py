# -*- coding: utf-8 -*-
from django import forms
from apps.generic.models import Usuario

default_error_message = {
    'required': 'Este campo é obrigatorio',
    'invalid': 'Valor invalido'
}

class RegistryForm(forms.ModelForm):


    class Meta:
        model = Usuario
        exclude = ('status','is_admin','last_access_ip','last_login')
        widgets = {
            'password': forms.PasswordInput(),
        }
        error_messages = {
            'password':default_error_message,
            'name':default_error_message,
            'sobrenome':default_error_message,
            'cpf':default_error_message,
            'telefone':default_error_message,
            'nascimento':default_error_message,
            'email':default_error_message,
        }
