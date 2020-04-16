# Imports para API V1
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

# Imports para API V2
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

from .permissions import IsSuperUser

"""
API V1
"""


class CursosAPIView(ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # Método get_queryset() é usado pra retornar uma lista
    # Lista avaliacoes vinculadas a um determinado curso
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # Método get_object() retorna apenas um objeto
    # Retorna uma determinada avaliacao de um curso
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    # Herda as permissões de acordo com permissões do Model User, porém obedecendo
    # a hierarquia de classe... IsSuperUser é chamada antes do que a ModelPermissions.
    permission_classes = (IsSuperUser, permissions.DjangoModelPermissions, )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # Criando nova subrota (cursos/<id>/avaliacoes<id>)
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):

        curso = self.get_object()
        # a expressão curso.avaliacoes.all() vem lá do ForeignKey do Model Avaliacao
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)

    """ Método se for usar paginação nas avaliações dentro de cada curso
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        # Configurando paginação para avaliações
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    """

# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer

# ViewSet Customizada
class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
   ):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
