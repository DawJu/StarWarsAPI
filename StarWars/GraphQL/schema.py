import django_filters
import graphene
from graphene_django.filter.fields import \
    DjangoFilterConnectionField  # type: ignore

import StarWars.GraphQL.mutations
from StarWars.GraphQL.model_nodes import (CharacterMovieNode, CharacterNode,
                                          MovieNode)
from StarWars.models import CharacterMovie


class CharacterMovieFilter(django_filters.FilterSet):
    character_name = django_filters.CharFilter(
        field_name="character__name", lookup_expr="icontains"
    )
    movie_name = django_filters.CharFilter(
        field_name="movie__name", lookup_expr="icontains"
    )
    movie_episode = django_filters.NumberFilter(field_name="movie__episode")

    class Meta:
        model = CharacterMovie
        fields = ["character_name", "movie_name", "movie_episode"]


class Query(graphene.ObjectType):
    characters = DjangoFilterConnectionField(CharacterNode)
    movies = DjangoFilterConnectionField(MovieNode)
    character_movies = DjangoFilterConnectionField(
        CharacterMovieNode, filterset_class=CharacterMovieFilter
    )


class Mutation(StarWars.GraphQL.mutations.Mutation, graphene.ObjectType):
    pass
