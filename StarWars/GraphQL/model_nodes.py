import graphene
from graphene_django import DjangoObjectType

from StarWars.models import Character, Movie, CharacterMovie


class CharacterNode(DjangoObjectType):
    class Meta:
        model = Character
        filter_fields = {
            "name": ["exact", "istartswith", "icontains"],
            "species": ["exact", "istartswith", "icontains"],
            "gender": ["exact", "istartswith", "icontains"],
            "age": ["exact"]
        }
        interfaces = (graphene.relay.Node,)


class MovieNode(DjangoObjectType):
    class Meta:
        model = Movie
        filter_fields = {
            "name": ["exact", "istartswith", "icontains"],
            "episode": ["exact"],
            "release_year": ["exact"]
        }
        interfaces = (graphene.relay.Node,)


class CharacterMovieNode(DjangoObjectType):
    class Meta:
        model = CharacterMovie
        filter_fields = ["character", "movie"]
        interfaces = (graphene.relay.Node,)
