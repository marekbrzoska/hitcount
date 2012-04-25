#-*- coding=utf-8 -*- 

from django.http import HttpResponseRedirect, HttpResponse
from models import Hit


def hit(request):
    ip = request.META['REMOTE_ADDR']
    url = request.build_absolute_uri()
    x = '{0} ({1}), {2} ({3})'.format(ip, str(type(ip)), url, str(type(url)))
    print x
    Hit.objects.create(ip=ip, url=url)
    return HttpResponse(x)
    return HttpResponseRedirect('http://planizer.pl')
