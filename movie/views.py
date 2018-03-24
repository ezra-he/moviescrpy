# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse


def hello(request):
    data = {'aaa':'bbb'}
    print  data
    return HttpResponse("<H1>Hello,World</H1>")

