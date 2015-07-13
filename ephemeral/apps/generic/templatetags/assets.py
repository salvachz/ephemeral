#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import re
import simplejson
from django.core.serializers import serialize
from django.db.models.query import QuerySet
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

def dictionary(dict, key):    
    try:
        return dict[key]
    except KeyError:
        try:
            return dict[str(key)]
        except:
            print 'error on dictionary: ',dict,key
            return ''

def multiply(value1, value2):
    if not value1 or not value2:
        return -1
    return float(value1) * float(value2)

def ortag(value1, value2):
    return value1 or value2

def jsonify(object):
    if isinstance(object, QuerySet):
        return serialize('json', object)
    return simplejson.dumps(object)


register.simple_tag(version)
register.filter('jsonify', jsonify)
register.filter(aklogo)
register.filter(dictionary)
register.filter(multiply)
