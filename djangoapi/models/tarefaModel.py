from django.db import models

# Importa os modelos 'Aluno' e 'Disciplina' de outros módulos.
from djangoapi.models.alunoModel import Aluno
from djangoapi.models.disciplinaModel import Disciplina

class Tarefa(models.Model):

    titulo = models.CharField(max_length=70)
    descricao = models.CharField(max_length=255)
    data_entrega = models.DateField()
    status = models.BooleanField(default=False)
    
    # Define um relacionamento muitos para um (ForeignKey) com o modelo 'Aluno'.
    # 'on_delete=models.CASCADE' especifica que, se o aluno associado for excluído, a tarefa também será excluída.
    # 'blank=False' e 'null=False' indicam que este campo é obrigatório e não pode ser deixado em branco ou nulo.
    aluno_delegado = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=False, null=False)
    
    # Define um relacionamento muitos para muitos (ManyToMany) com o modelo 'Disciplina'.
    # Isso permite que uma tarefa esteja associada a várias disciplinas.
    disciplinas = models.ManyToManyField(Disciplina)
    

    def __str__(self):
        return self.titulo
