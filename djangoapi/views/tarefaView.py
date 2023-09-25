from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djangoapi.models.tarefaModel import Tarefa
from djangoapi.serializers.tarefaSerializer import TarefaSerializer

class TarefaView(APIView):
    
    def get(self, request, id=None):

        if id is not None:
            try:
                tarefa = Tarefa.objects.get(pk=id)  # Tenta encontrar o Tarefa pelo ID
                serializer = TarefaSerializer(tarefa, many=False)
                return Response(serializer.data)
        
            except Tarefa.DoesNotExist:
                return Response({'detail': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        else:
            tarefas = Tarefa.objects.all()
            serializer = TarefaSerializer(tarefas, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            tarefa = Tarefa.objects.get(pk=id)  # Tenta encontrar o Tarefa pelo ID
        except Tarefa.DoesNotExist:
            return Response({'detail': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TarefaSerializer(tarefa, data=request.data)  # Passa o Tarefa encontrado e os dados da requisição para o serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            tarefa = Tarefa.objects.get(pk=id)  # Tenta encontrar o Tarefa pelo ID
        except Tarefa.DoesNotExist:
            return Response({'detail': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        Tarefa.delete()  # Exclui o Tarefa encontrado
        return Response({'detail': 'Tarefa excluída com sucesso'}, status=status.HTTP_204_NO_CONTENT)
