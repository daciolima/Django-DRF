from rest_framework import serializers

from .models import Curso, Avaliacao


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        )


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            # Campo email será apresentado somente no momento do cadastro(write_only=True)
            'email': {'write_only': True}
        }

        # Model que pertence a esse Serializer
        model = Avaliacao

        # Campos que serão apresentados
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )



