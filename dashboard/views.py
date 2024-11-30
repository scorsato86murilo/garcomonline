from django.shortcuts import render


def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html')
    elif request.method == 'POST':
        return render(request, 'dashboard.html')


def comandas(request):
    if request.method == 'GET':
        return render(request, 'comandas.html')
    elif request.method == 'POST':
        return render(request, 'comandas.html')


def cardapio(request):
    if request.method == 'GET':
        return render(request, 'cardapio.html')
    elif request.method == 'POST':
        return render(request, 'cardapio.html')


def cadastrar_clientes(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_clientes.html')
    elif request.method == 'POST':
        return render(request, 'cadastrar_clientes.html')






def adicionar_produtos(request):
    if request.method == 'GET':
        return render(request, 'adicionar_produtos.html')
    elif request.method == 'POST':
        return render(request, 'adicionar_produtos.html')