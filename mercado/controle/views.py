from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    print(request.method)

    if request.method == 'post':
    
        nome = request.post.get("nome")
        estoque_atual = request.post.get("estoque_atual")
        print(nome)
        print(estoque_atual)

    return render(request, "controle/home.html")