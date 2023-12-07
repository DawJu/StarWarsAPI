import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from .models import Character


class CharacterNode(DjangoObjectType):
    # id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Character
        filter_fields = {
            'character_id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'species': ['exact', 'icontains'],
            'gender': ['exact'],
            'age': ['exact']
        }
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    characters = graphene.List(CharacterNode)

    def resolve_characters(self, info):
        return Character.objects.all()


class CreateCharacter(graphene.Mutation):
    character = graphene.Field(CharacterNode)

    class Arguments:
        name = graphene.String()
        species = graphene.String()
        gender = graphene.String()
        age = graphene.Int()

    def mutate(self, info, name, species, gender, age):
        character = Character(name=name, species=species, gender=gender, age=age)
        character.save()
        return CreateCharacter(character=character)


class UpdateCharacter(graphene.Mutation):
    character = graphene.Field(CharacterNode)

    class Arguments:
        character_id = graphene.ID()
        name = graphene.String()
        species = graphene.String()
        gender = graphene.String()
        age = graphene.Int()

    def mutate(self, info, character_id, name='', species='', gender='', age=-1):
        character = Character.objects.get(character_id=character_id)
        if name != '':
            character.name = name
        if species != '':
            character.species = species
        if gender != '':
            character.gender = gender
        if age != -1:
            character.age = age
        character.save()
        return UpdateCharacter(character=character)


class DeleteCharacter(graphene.Mutation):
    # ok = graphene.Boolean()
    character_id = graphene.ID()

    class Arguments:
        character_id = graphene.ID()

    def mutate(self, info, character_id):
        character = Character.objects.get(character_id=character_id)
        character.delete()
        return DeleteCharacter(character_id=character_id)


class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
    update_character = UpdateCharacter.Field()
    delete_character = DeleteCharacter.Field()
