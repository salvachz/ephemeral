from django.conf.urls import patterns, include, url, handler404
from django.views.generic import TemplateView
from django.contrib import admin
from apps.generic import models as genericModels
from apps.generic import views as genericViews
from settings import settings
# -*- coding: utf-8 -*-

admin.site.register([
	genericModels.Produto,
	genericModels.Categoria,
	genericModels.Marca,
    genericModels.Usuario,
])
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', genericViews.LoginView.as_view(), name='login'),
    url(r'^registry/$', genericViews.RegistryView.as_view(), name='registry'),
    url(r'^$', genericViews.HomeView.as_view(), name='home'),
    url(r'^produto/(?P<slug>.*)$', genericViews.ProductDetailView.as_view(), name='detail'),
)


urlpatterns += patterns('', (
    r'^products-img/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.PRODUCT_ROOT}
))