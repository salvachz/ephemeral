# -*- coding: utf-8 -*-
from django import forms
from apps.generic.models import Usuario

default_error_message = {
    'required': 'Este campo é obrigatorio',
    'invalid': 'Valor invalido'
}

class UserForm(forms.ModelForm):


    class Meta:
        model = Usuario
        exclude = ('status','is_admin','last_access_ip','last_login','password')
        widgets = {
            'password': forms.PasswordInput(),
        }
        error_messages = {
            'password':default_error_message,
            'nome':default_error_message,
            'email':default_error_message,
        }