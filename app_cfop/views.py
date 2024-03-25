from django.shortcuts import render
from .models import CfopEntrada, CfopCompra
def home(request):
    return render(request, 'home.html')

def listarDados(request):
    

    cfopEntrada = CfopEntrada.objects.all()
    cfopCompra = CfopCompra.objects.all()
    dados = {'cfopEntrada': cfopEntrada, 'cfopCompra': cfopCompra}

    return render(request, 'listarDados.html', dados)