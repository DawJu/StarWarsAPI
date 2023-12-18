import graphene
from graphene_django import DjangoObjectType

from StarWars.models import Character, Movie


class CharacterNode(DjangoObjectType):
    class Meta:
        model = Character
        filter_fields = ["name", "species", "gender", "age"]
        interfaces = (graphene.relay.Node,)


class MovieNode(DjangoObjectType):
    class Meta:
        model = Movie
        filter_fields = ["name", "episode", "release_year"]
        interfaces = (graphene.relay.Node,)
