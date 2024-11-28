from django.shortcuts import render
from .models import LadoEsquerdo, LadoDireito

def index(request):
    if request.method == 'GET':
        lado_esquerdo = LadoEsquerdo.objects.first()
        lado_direito = LadoDireito.objects.first()


        contexto = {
            'lado_esquerdo': lado_esquerdo,
            'lado_direito': lado_direito,
        }
        return render(request, 'index.html', contexto)

    elif request.method == 'POST':
        # Adicione lógica para atualizar os dados do banco de dados, se necessário.
        pass
