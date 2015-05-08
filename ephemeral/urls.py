from django.conf.urls import patterns, include, url, handler404
from django.views.generic import TemplateView
from django.contrib import admin
from settings import settings


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(), name='home'),
)
