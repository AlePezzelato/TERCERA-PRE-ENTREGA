from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=150)
    apeliido = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(null=True)

class Docente(models.Model):
    ...

class Materia(models.Model):
    ...
    
