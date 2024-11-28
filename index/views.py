from django.shortcuts import render
from .models import LadoEsquerdo, LadoDireito, NomeEstabelecimento, TamanhoImg


def index(request):
    if request.method == 'GET':
        lado_esquerdo = LadoEsquerdo.objects.first()
        lado_direito = LadoDireito.objects.first()
        nome = NomeEstabelecimento.objects.first()
        tamanho = TamanhoImg.objects.first()


        contexto = {
            'lado_esquerdo': lado_esquerdo,
            'lado_direito': lado_direito,
            'nome': nome,
            'tamanho': tamanho,
        }
        return render(request, 'index.html', contexto)

    elif request.method == 'POST':
        # Aqui você pode processar dados enviados via POST, por exemplo:
        # dados = request.POST['campo']
        pass
