# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(render(request, 'common/index.html'))

def post(request,suburl):
	return HttpResponse(render(request, 'app_blog/index.html'))

def list(request):
	orderby = request.GET.get('orderby',None)
	p = request.GET.get('p',None)
	return HttpResponse(render(request, 'app_blog/index.html'))

def editmd(request):
    pass