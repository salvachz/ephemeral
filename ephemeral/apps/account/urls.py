from django.conf.urls import patterns, url
from apps.account import views as accountViews
from settings import settings
# -*- coding: utf-8 -*-

urlpatterns = patterns('',
    url(r'^$', accountViews.AccountHomeView.as_view(), name='account-home'),
    url(r'^minha-conta/$', accountViews.AccountMyAccountView.as_view(), name='account-myAccount'),
    url(r'^sair/$', accountViews.AccountLogoutView.as_view(), name='account-logout'),
    url(r'^finalizar/$', accountViews.AccountCheckoutView.as_view(), name='account-checkout'),

)
