from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from core.services import SearchService

def index(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render({},request))
    

def search(request):
    service = SearchService(request.GET['source'])
    service.search(request.GET['q'])
    if len(service.store) <= 0:
        return HttpResponse("A consulta retornou vazia")
    else:
        return HttpResponse(service.store)