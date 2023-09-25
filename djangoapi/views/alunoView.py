from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djangoapi.models.alunoModel import Aluno
from djangoapi.serializers.alunoSerializer import AlunoSerializer

class AlunoView(APIView):        

    def get(self, request, id=None):

        if id is not None:
            try:
                aluno = Aluno.objects.get(pk=id)  # Tenta encontrar o aluno pelo ID
                serializer = AlunoSerializer(aluno, many=False)
                return Response(serializer.data)
        
            except Aluno.DoesNotExist:
                return Response({'detail': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        else:
            alunos = Aluno.objects.all()
            serializer = AlunoSerializer(alunos, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            aluno = Aluno.objects.get(pk=id)  # Tenta encontrar o aluno pelo ID
        except Aluno.DoesNotExist:
            return Response({'detail': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AlunoSerializer(aluno, data=request.data)  # Passa o aluno encontrado e os dados da requisição para o serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            aluno = Aluno.objects.get(pk=id)  # Tenta encontrar o aluno pelo ID
        except Aluno.DoesNotExist:
            return Response({'detail': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        aluno.delete()  # Exclui o aluno encontrado
        return Response({'detail': 'Aluno excluído com sucesso'}, status=status.HTTP_204_NO_CONTENT)

    