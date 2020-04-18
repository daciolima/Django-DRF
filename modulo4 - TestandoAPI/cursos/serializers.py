from rest_framework import serializers

from .models import Curso, Avaliacao

# Importação de função para média
from django.db.models import Avg


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



    # Funcao para criar validações no campo ( Função deve iniciar com validate_nomeDoCampo)
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):  # 1, 2, 3, 4, 5
            return valor
        raise serializers.ValidationError('Validação deve ser entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):

    # Nested Relationship (Curso aninhado com suas respectivas avaliações )
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Criação de objeto para incrementar a customização de serealização de dados
    media_avaliacoes = serializers.SerializerMethodField()

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
            'avaliacoes',
            # Campo criado para customização de serializaçao deve ter um objeto criado do tipo MethodField
            'media_avaliacoes'
        )

    # Funcao para criar serialização customizada (Função deve iniciar com get_nomeDoCampo)
    # OBS: Dependendo do tamanho dos dados pode ser recomendado fazer um campo no model
    # e seta-los com um signals no lugar desse procedimento usando MethodField
    def get_media_avaliacoes(self, obj):
        # Funçao Avg calcula os retornos do relacionamento do campo curso no model Avaliacoes e
        # retornar o total pela função get
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2


