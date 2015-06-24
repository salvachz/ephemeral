# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    form_name = 'login'

    email = forms.CharField(label='email', min_length=3, max_length=255)
    password = forms.CharField(label='senha',
        error_messages={'invalid': 'Senha invalida'},
        widget=forms.PasswordInput())
