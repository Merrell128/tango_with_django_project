# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):

    context_dict = {'boldmessage': "Crunchy, cream, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context = context_dict)
