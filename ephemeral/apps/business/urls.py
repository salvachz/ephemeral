from django.conf.urls import patterns, url
from apps.business import views as businessViews
from settings import settings
# -*- coding: utf-8 -*-

urlpatterns = patterns('',
    url(r'^$', businessViews.BusinessHomeView.as_view(), name='business-home'),
    url(r'^dashboard/$', businessViews.BusinessDashboardView.as_view(), name='business-dashboard'),
    url(r'^conversao/$', businessViews.BusinessCartConversionView.as_view(), name='business-cartConversion'),

)
