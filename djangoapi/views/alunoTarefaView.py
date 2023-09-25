from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djangoapi.models.alunoModel import Aluno
from djangoapi.models.tarefaModel import Tarefa
from djangoapi.serializers.tarefaSerializer import TarefaSerializer

class AlunoTarefasView(APIView):
    
    def get(self, request, aluno_id):
        #Busca o aluno pelo ID
        try:
            aluno = Aluno.objects.get(pk=aluno_id)
        except Aluno.DoesNotExist:
            return Response({'detail': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        #Retorna todas tarefa com esse ID associado
        tarefas = Tarefa.objects.filter(aluno_delegado=aluno)
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    
