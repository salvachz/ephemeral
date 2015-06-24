#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import re
from datetime import datetime
from django import template
from django.conf import settings
from django.templatetags.static import static
register = template.Library()

g_filter = {}
def filter_url(value, _type):
    global g_filter
    result = []
    if not isinstance(g_filter,dict):
        g_filter = {}
    c_filter = g_filter.copy()
    c_filter[_type] = value
    for k in c_filter:
        if not c_filter[k]:
            continue
        result.append("%s=%s" % (k, c_filter[k].id))
    return '?%s' % '&'.join(result)

def setfilter(_filter):
    global g_filter
    if not g_filter:
        g_filter = _filter
    else:
        for k in _filter:
            g_filter[k] = _filter[k]
    return ''


register.filter(filter_url)
register.simple_tag(setfilter)
