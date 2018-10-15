# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
def index(request):
    return render(request, 'personal/index.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me:','	shaorz@gmail.com']})

def about(request):
	return render(request, 'personal/about.html')


