from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djangoapi.models.disciplinaModel import Disciplina
from djangoapi.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaView(APIView):
    
    def get(self, request, id=None):

        if id is not None:
            try:
                disciplina = Disciplina.objects.get(pk=id)  # Tenta encontrar a Disciplina pelo ID
                serializer = DisciplinaSerializer(disciplina, many=False)
                return Response(serializer.data)
        
            except Disciplina.DoesNotExist:
                return Response({'detail': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        else:
            disciplinas = Disciplina.objects.all()
            serializer = DisciplinaSerializer(disciplinas, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            disciplina = Disciplina.objects.get(pk=id)  # Tenta encontrar a Disciplina pelo ID
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DisciplinaSerializer(disciplina, data=request.data)  # Passa a Disciplina encontrada e os dados da requisição para o serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            disciplina = Disciplina.objects.get(pk=id)  # Tenta encontrar a Disciplina pelo ID
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        Disciplina.delete()  # Exclui a Disciplina encontrado
        return Response({'detail': 'Disciplina excluída com sucesso'}, status=status.HTTP_204_NO_CONTENT)
