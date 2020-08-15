from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

def HomeView(request):
    text = _('Hello World')
    return HttpResponse(text)