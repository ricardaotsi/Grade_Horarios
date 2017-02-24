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
            c = Curso()
            c.nome_curso = formulario.cleaned_data['nome_curso']
            c.save()
            if formulario.cleaned_data['materias']:
                c.materia = formulario.cleaned_data['materias']
                c.save()
    else:
        formulario = CursoForm()
    return render(request, 'grade/curso.html', {'formulario':formulario, 'curso':curso})

@login_required
def cadastromateria(request):
    materia = Materia.objects.order_by('nome_materia')
    if request.method == "POST":
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            temp_materia = formulario.save(commit=False)
            temp_materia.save()
    else:
        formulario = MateriaForm()
    return render(request, 'grade/materia.html', {'formulario': formulario, 'materia': materia})