from django.contrib import admin
from django.urls import path
from djangoapi.views.alunoView import AlunoView 
from djangoapi.views.disciplinaView import DisciplinaView
from djangoapi.views.tarefaView import TarefaView
from djangoapi.views.alunoTarefaView import AlunoTarefasView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alunos/', AlunoView.as_view()),  # Rota para manipular alunos (GET e POST)
    path('api/alunos/<int:id>/', AlunoView.as_view()),  # Rota para manipular aluno por ID (PUT e DELETE)
    path('api/disciplinas/', DisciplinaView.as_view()),  # Rota para manipular disciplinas (GET e POST)
    path('api/disciplinas/<int:id>/', DisciplinaView.as_view()),  # Rota para manipular disciplina por ID (PUT e DELETE)
    path('api/tarefas/', TarefaView.as_view()),  # Rota para manipular tarefas (GET e POST)
    path('api/tarefas/<int:id>/', TarefaView.as_view()),  # Rota para manipular tarefa por ID (PUT e DELETE)
    path('api/alunos/<int:aluno_id>/tarefas/', AlunoTarefasView.as_view()),  # Rota para listar tarefas de um aluno (GET)
]
