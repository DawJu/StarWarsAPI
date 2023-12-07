import graphene
import StarWars.schema

class Query(StarWars.schema.Query, graphene.ObjectType):
    pass

class Mutation(StarWars.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
