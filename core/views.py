from django.shortcuts import render

# Create your views here.
def index(request):
    print(dir(request.user))
    print(f"User: {request.user}")

    if str(request.user) == "AnonymousUser":
        teste = "Usuario não logado"
    else:
        teste = "Usuario logado"
    context ={
        'course': 'Progamming Web with Django Framework',
        'another' : 'Django is cool!',
        'logado' : teste
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')