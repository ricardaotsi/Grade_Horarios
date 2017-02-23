from django import forms

from .models import *

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nome_curso', 'materia',)

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('nome_materia',)