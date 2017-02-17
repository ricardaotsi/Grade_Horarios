from django.shortcuts import render
#from .models import Professor, Sala, Curso
# Create your views here.
def ensalamento(request):
#    profs = Professor.objects.order_by('nome')
#    salas = Sala.objects.order_by('sala')
#    cursos= Curso.objects.order_by('curso')
    return render(request, 'grade/base.html')#, {'profs':profs, 'salas':salas, 'cursos':cursos})