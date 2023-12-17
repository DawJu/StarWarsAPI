import graphene

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
        character_id = graphene.ID(required=True)
        name = graphene.String()
        species = graphene.String()
        gender = graphene.String()
        age = graphene.Int()

    def mutate(self, info, character_id, **kwargs):
        character = CharacterService().update_character(character_id, **kwargs)
        return UpdateCharacter(character=character)


class DeleteCharacter(graphene.Mutation):
    character_id = graphene.ID()

    class Arguments:
        character_id = graphene.ID()

    def mutate(self, info, character_id):
        character_id = CharacterService().delete_character(character_id)
        return DeleteCharacter(character_id=character_id)


class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
    update_character = UpdateCharacter.Field()
    delete_character = DeleteCharacter.Field()
