import graphene
from graphene_django import DjangoObjectType

from StarWars.models import Character


class CharacterNode(DjangoObjectType):
    class Meta:
        model = Character
        filter_fields = ["name", "species", "gender", "age"]
        interfaces = (graphene.relay.Node,)
