from rest_framework import serializers
from djangoapi.models.disciplinaModel import Disciplina

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'