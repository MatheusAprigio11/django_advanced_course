from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    context ={
        'course': 'Progamming Web with Django Framework',
        'another' : 'Django is cool!',
        'produtos' : produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    # product = Produto.objects.get(id=pk)
    product = get_object_or_404(Produto, id=pk) # BUSCA O ID QUE O USUARIO REQUISITOU, CASO NAO ENCONTRE, DEVOLVA 404
    context = {
        'produto': product
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type ='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)