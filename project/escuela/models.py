from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=150)
    apeliido = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(null=True)
    materia_id = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True)
    docente_id = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    nota = models.CharField(max_length=20)
    

class Docente(models.Model):
    nombre = models.CharField(max_length=150)
    apeliido = models.CharField(max_length=150)
    materia_id = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True)
        
class Materia(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    codigo = models.CharField(max_length=10)
    
