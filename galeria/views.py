from django.shortcuts import render
from django.http import HttpResponse

#funcao para receber ou redirecionar pagina
def index(request): 
    return render(request, 'galeria/index.html')

def imagem(request): 
    return render(request, 'galeria/imagem.html')