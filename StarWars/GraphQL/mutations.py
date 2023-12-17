import graphene
from graphql_relay.node.node import from_global_id

from StarWars.GraphQL.model_nodes import CharacterNode
from StarWars.services import CharacterService


class CreateCharacter(graphene.Mutation):
    character = graphene.Field(CharacterNode)

    class Arguments:
        name = graphene.String(required=True)
        species = graphene.String()
        gender = graphene.String(required=True)
        age = graphene.Int(required=True)

    def mutate(self, info, name, gender, age, species=None):
        character = CharacterService().create_character(name, gender, age, species)
        return CreateCharacter(character=character)


class UpdateCharacter(graphene.Mutation):
    character = graphene.Field(CharacterNode)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        species = graphene.String()
        gender = graphene.String()
        age = graphene.Int()

    def mutate(self, info, id, **kwargs):
        character = CharacterService().update_character(from_global_id(id)[1], **kwargs)
        return UpdateCharacter(character=character)


class DeleteCharacter(graphene.Mutation):
    id = graphene.ID()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        CharacterService().delete_character(from_global_id(id)[1])
        return DeleteCharacter(id=id)


class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
    update_character = UpdateCharacter.Field()
    delete_character = DeleteCharacter.Field()
