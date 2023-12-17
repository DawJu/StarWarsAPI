import graphene

import StarWars.GraphQL.schema


class Query(StarWars.GraphQL.schema.Query, graphene.ObjectType):
    pass


class Mutation(StarWars.GraphQL.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
