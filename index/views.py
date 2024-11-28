from django.shortcuts import render
from .models import LadoEsquerdo, LadoDireito, NomeEstabelecimento, TamanhoImg, TituloPagina


def index(request):
    if request.method == 'GET':
        lado_esquerdo = LadoEsquerdo.objects.first()
        lado_direito = LadoDireito.objects.first()
        nome = NomeEstabelecimento.objects.first()
        tamanho = TamanhoImg.objects.first()
        titulo =TituloPagina.objects.first()


        contexto = {
            'lado_esquerdo': lado_esquerdo,
            'lado_direito': lado_direito,
            'nome': nome,
            'tamanho': tamanho,
            'titulo': titulo,
        }
        return render(request, 'index.html', contexto)

    elif request.method == 'POST':
        # Aqui você pode processar dados enviados via POST, por exemplo:
        # dados = request.POST['campo']
        pass
