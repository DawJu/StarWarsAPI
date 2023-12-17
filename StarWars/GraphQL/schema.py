import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from StarWars.GraphQL.model_nodes import CharacterNode
import StarWars.GraphQL.mutations


class Query(graphene.ObjectType):
    characters = DjangoFilterConnectionField(CharacterNode)


class Mutation(StarWars.GraphQL.mutations.Mutation, graphene.ObjectType):
    pass
