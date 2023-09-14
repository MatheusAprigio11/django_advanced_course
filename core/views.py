from django.shortcuts import render

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
    product = Produto.objects.get(id=pk)
    context = {
        'produto': product
    }
    return render(request, 'produto.html', context)