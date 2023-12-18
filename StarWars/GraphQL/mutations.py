import graphene
from graphql_relay.node.node import from_global_id

from StarWars.GraphQL.model_nodes import CharacterNode, MovieNode, CharacterMovieNode
from StarWars.services import CharacterService, MovieService, CharacterMovieService


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


class CreateMovie(graphene.Mutation):
    movie = graphene.Field(MovieNode)

    class Arguments:
        name = graphene.String(required=True)
        episode = graphene.Int()
        release_year = graphene.Int()

    def mutate(self, info, name, episode=None, release_year=None):
        movie = MovieService().create_movie(name, episode, release_year)
        return CreateMovie(movie=movie)


class UpdateMovie(graphene.Mutation):
    movie = graphene.Field(MovieNode)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        episode = graphene.Int()
        release_year = graphene.Int()

    def mutate(self, info, id, **kwargs):
        movie = MovieService().update_movie(from_global_id(id)[1], **kwargs)
        return UpdateMovie(movie=movie)


class DeleteMovie(graphene.Mutation):
    id = graphene.ID()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        MovieService().delete_movie(from_global_id(id)[1])
        return DeleteMovie(id=id)


class CreateCharacterMovie(graphene.Mutation):
    character_movie = graphene.Field(CharacterMovieNode)

    class Arguments:
        character_id = graphene.ID(required=True)
        movie_id = graphene.ID(required=True)

    def mutate(self, info, character_id, movie_id):
        character_movie = CharacterMovieService().create_character_movie(
            from_global_id(character_id)[1], from_global_id(movie_id)[1]
        )
        return CreateCharacterMovie(character_movie=character_movie)


class DeleteCharacterMovie(graphene.Mutation):
    id = graphene.ID()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        CharacterMovieService().delete_character_movie(from_global_id(id)[1])
        return DeleteCharacterMovie(id=id)


class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
    update_character = UpdateCharacter.Field()
    delete_character = DeleteCharacter.Field()

    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()

    create_character_movie = CreateCharacterMovie.Field()
    delete_character_movie = DeleteCharacterMovie.Field()
