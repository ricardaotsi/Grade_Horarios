from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import *
from .models import *

def ensalamento(request):
    return render(request, 'grade/ensalamento.html')

@login_required
def grade(request):
    return render(request, 'grade/grade.html')

@login_required
def cadastrocurso(request):
    curso = Curso.objects.order_by('nome_curso')
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            temp_curso = formulario.save(commit=False)
            temp_curso.save()
    else:
        formulario = CursoForm()
    return render(request, 'grade/curso.html', {'formulario':formulario, 'curso':curso})