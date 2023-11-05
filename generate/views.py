from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def card(request):
  template = loader.get_template('card.html')
  return HttpResponse(template.render())