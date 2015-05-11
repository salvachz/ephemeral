#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import re
from datetime import datetime
from django import template
from django.conf import settings
from django.templatetags.static import static
register = template.Library()

version_cache = {}
def version(path_string):
    try:
        if path_string in version_cache:
            mtime = version_cache[path_string]
        else:
            mtime = os.path.getmtime(
                        os.path.join(settings.STATIC_ROOT, path_string)
                    )
            version_cache[path_string] = mtime

        return static('%s?%d' %(path_string,mtime) )
    except:
        return static('%s?%s' %(path_string,datetime.now().strftime('%s')))


def aklogo(path, imgid):
    try:
        path, extension = path.split('.')
        return '%s_%s.%s' % (path, imgid, extension)
    except:
        # raise
        return ''

register.simple_tag(version)
register.filter(aklogo)