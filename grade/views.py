from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def ensalamento(request):
    return render(request, 'grade/ensalamento.html')

@login_required
def teste(request):
    return render(request, 'grade/teste.html')
