from django.shortcuts import render, httpsResponse

# Create your views here. 
def index(request):
    return httpsResponse("<h1>Página inicial do estoque.</h1>")

