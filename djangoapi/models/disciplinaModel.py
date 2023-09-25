from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.name