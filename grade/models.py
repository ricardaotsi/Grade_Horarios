from django.db import models

class Dia_Semana(models.Model):
    dia_semana = models.CharField(max_length=8)

class Horario(models.Model):
    horario = models.IntegerField()

class Sala(models.Model):
    sala = models.CharField(max_length=50)

class Materia(models.Model):
    nome_materia = models.CharField(max_length=50)

class Curso(models.Model):
    nome_curso = models.CharField(max_length=50)
    materia = models.ManyToManyField(Materia)

class Professor(models.Model):
    nome_professor = models.CharField(max_length=50)
    materia = models.ManyToManyField(Materia)

class Turno(models.Model):
    turno = models.CharField(max_length=10)

class Semestre(models.Model):
    semestre = models.IntegerField()

class Turma(models.Model):
    periodo = models.IntegerField()
    turno = models.ForeignKey(Turno)
    curso = models.ForeignKey(Curso)
    semestre = models.ForeignKey(Semestre)

class Grade(models.Model):
    dia_semana = models.ForeignKey(Dia_Semana)
    horario = models.ForeignKey(Horario)
    materia = models.ForeignKey(Materia)
    turma = models.ForeignKey(Turma)
    sala = models.ForeignKey(Sala)
