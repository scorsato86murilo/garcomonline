from django.shortcuts import render



def area_membros(request):
    if request.method == 'GET':
        return render(request, 'area_membros.html')
    elif request.method == 'POST':
        return render(request, 'area_membros.html')

def logar_membro(request):
    if request.method == 'GET':
        return render(request, 'logar_membro.html')
    elif request.method == 'POST':
        return render(request, 'logar_membro.html')