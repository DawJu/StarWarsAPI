import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from StarWars.GraphQL.model_nodes import CharacterNode, MovieNode
import StarWars.GraphQL.mutations


class Query(graphene.ObjectType):
    characters = DjangoFilterConnectionField(CharacterNode)
    movies = DjangoFilterConnectionField(MovieNode)


class Mutation(StarWars.GraphQL.mutations.Mutation, graphene.ObjectType):
    pass
