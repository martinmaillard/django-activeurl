# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from django.conf.urls.defaults import patterns, url
except ImportError:
    from django.conf.urls import patterns, url
from django.http import HttpResponse
from django.shortcuts import render


def view(request):
    return HttpResponse()


def djnago_template_view(request):
    return render(request, 'django.html', {})


def jinja_template_view(request):
    return render(request, 'jinja.html', {})


urlpatterns = patterns(
    '',
    url(r'^$', view),
    url(r'^template/django/$', djnago_template_view),
    url(r'^template/jinja/$', jinja_template_view),
    url(r'^page/$', view),
    url(r'^menu/$', view),
    url(r'^menu/submenu/$', view),
    url(r'^страница/$', view),
    url(r'^другая_страница/$', view, name='non-ascii-reverse')
)
