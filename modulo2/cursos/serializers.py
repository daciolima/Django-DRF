from rest_framework import serializers

from .models import Curso, Avaliacao


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


class CursoSerializer(serializers.ModelSerializer):

    # Nested Relationship (Curso aninhado com suas respectivas avaliações )
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    """
    # HyperLinked Related Field (Curso aninhado com suas respectivas avaliações em forma de link )
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail'
    )
    """
    # Primary Key Related Field (Curso aninhado com suas respectivas avaliações retornando só ID )
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)



    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )

