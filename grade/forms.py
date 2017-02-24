from django import forms

from .models import *

class CursoForm(forms.Form):
    nome_curso = forms.CharField(max_length=50)
    materias = forms.ModelMultipleChoiceField(queryset=Materia.objects.order_by('nome_materia'), required=False)

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('nome_materia',)