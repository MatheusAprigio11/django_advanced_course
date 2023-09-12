from django.shortcuts import render

# Create your views here.
def index(request):
    context ={
        'course': 'Progamming Web with Django Framework',
        'another' : 'Django is cool!'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')