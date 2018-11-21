# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from app_webtrans.models import APP_FILE_ROOT,APP_TEMPLETE_ROOT
#from dwebsocket import accept_websocket,require_websocket
from mysite.settings import BAIDUMAP

def index(request):
    return HttpResponseRedirect(reverse('app_webtrans_websocket'))

def websocket(request):
    return HttpResponse(render(request, APP_TEMPLETE_ROOT+'index.html',{\
        'title':'图灵机器人',\
        'display':'websocket',\
        }))

def tcptrans(request):
    return HttpResponse(render(request, APP_TEMPLETE_ROOT+'index.html',{\
        'title':'即时通信',\
        'display':'tcptrans',\
        }))

def nat(request):
    return HttpResponse(render(request, APP_TEMPLETE_ROOT+'index.html',{\
        'title':'内网穿透',\
        'display':'nat',\
        }))

def wechat(request):
    return HttpResponse(render(request, APP_TEMPLETE_ROOT+'index.html',{\
        'title':'微信应用',\
        'display':'wechat',\
        }))

def map(request):
    return HttpResponse(render(request, APP_TEMPLETE_ROOT+'index.html',{\
        'title':'地图应用',\
        'display':'map',\
        'ak':BAIDUMAP['AK'],\
        }))

def proxy(request):
    url = request.GET.get('url', None)
    if url:
        try:
            headers = {
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'en',
                'Host': url.split('/')[2]
            }
            res=requests.get(url,headers=headers)
            return HttpResponse(res)
        except Exception as e:
            return HttpResponse(e)
        # return JsonResponse({'status':200})
    else:
        return HttpResponse(render(request, APP_TEMPLETE_ROOT+'index.html',{\
            'title':'代理访问',\
            'display':'proxy',\
            }))

# dwebsocket库中的BUG（可能是因为没有兼容python2）
# /usr/lib/python2.7/site-packages/dwebsocket/backends/default/websocket.py 把使用的queue库改为Queue
# /usr/lib/python2.7/site-packages/dwebsocket/backends/default/protocol.py 把data=bytes(data,'utf-8')改成data=bytes(data)
#@accept_websocket
def socket(request, type):
    if type == 'websocket' and request.is_websocket():
        request.websocket.send('[server]Welcome!'.encode('utf-8'))
        for message in request.websocket:  # websocket是一个持续接收客户端输入的生成器，不会阻塞
            request.websocket.send('[server]received'.encode('utf-8'))
    else:
        pass
