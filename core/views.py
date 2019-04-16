from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from core.services import SearchService

from core.models import Search

def index(request):
    template = loader.get_template('search.html')
    last_searchies = Search.objects.all()
    return render(request, 'search.html', {'searchies': last_searchies})
    

def search(request):
    response = None
    if request.GET['source'] != None and request.GET['q'] != None:
        register_search = Search(source=request.GET['source'], query=request.GET['q'])
        register_search.save()

        service = SearchService(request.GET['source'])
        service.search(request.GET['q'])
        if len(service.store) <= 0:
            response = "A consulta retornou vazia"
        else:
            response = service.store
    return render(request, 'results.html', { 'results': response, 'query': request.GET['q'], 'source': request.GET['source'] })