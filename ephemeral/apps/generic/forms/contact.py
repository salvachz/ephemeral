# -*- coding: utf-8 -*-
from django import forms
from apps.generic.models import Contato

default_error_message = {
    'required': 'Este campo é obrigatorio',
    'invalid': 'Valor invalido'
}

class ContactForm(forms.ModelForm):


    class Meta:
        model = Contato
        exclude = ('id','status')

        error_messages = {
            'assunto':default_error_message,
            'menssagem':default_error_message,
            'nome':default_error_message,
            'email':default_error_message,
        }
