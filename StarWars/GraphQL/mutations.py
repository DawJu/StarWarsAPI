import graphene
from graphql_relay.node.node import from_global_id

from StarWars.GraphQL.model_nodes import (CharacterMovieNode, CharacterNode,
                                          MovieNode)
from StarWars.services import (CharacterMovieService, CharacterService,
                               MovieService)


class CreateCharacter(graphene.Mutation):
    character = graphene.Field(CharacterNode)

    class Arguments:
        name = graphene.String(required=True)
        species = graphene.String()
        gender = graphene.String(required=True)
        age = graphene.Int(required=True)

    def mutate(
        self, info, name: str, gender: str, age: int, species: str | None = None
    ) -> "CreateCharacter":
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

    def mutate(self, info, id: str, **kwargs) -> "UpdateCharacter":
        character = CharacterService().update_character(from_global_id(id)[1], **kwargs)
        return UpdateCharacter(character=character)


class DeleteCharacter(graphene.Mutation):
    id = graphene.ID()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id: str) -> "DeleteCharacter":
        CharacterService().delete_character(from_global_id(id)[1])
        return DeleteCharacter(id=id)


class CreateMovie(graphene.Mutation):
    movie = graphene.Field(MovieNode)

    class Arguments:
        name = graphene.String(required=True)
        episode = graphene.Int()
        release_year = graphene.Int()

    def mutate(
        self,
        info,
        name: str,
        episode: int | None = None,
        release_year: int | None = None,
    ) -> "CreateMovie":
        movie = MovieService().create_movie(name, episode, release_year)
        return CreateMovie(movie=movie)


class UpdateMovie(graphene.Mutation):
    movie = graphene.Field(MovieNode)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        episode = graphene.Int()
        release_year = graphene.Int()

    def mutate(self, info, id: str, **kwargs) -> "UpdateMovie":
        movie = MovieService().update_movie(from_global_id(id)[1], **kwargs)
        return UpdateMovie(movie=movie)


class DeleteMovie(graphene.Mutation):
    id = graphene.ID()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id: str) -> "DeleteMovie":
        MovieService().delete_movie(from_global_id(id)[1])
        return DeleteMovie(id=id)


class CreateCharacterMovie(graphene.Mutation):
    character_movie = graphene.Field(CharacterMovieNode)

    class Arguments:
        character_name = graphene.String()
        character_id = graphene.ID()
        movie_name = graphene.String()
        movie_episode = graphene.Int()
        movie_id = graphene.ID()

    def mutate(self, info, **kwargs) -> "CreateCharacterMovie":
        character_movie = CharacterMovieService().create_character_movie(**kwargs)
        return CreateCharacterMovie(character_movie=character_movie)


class DeleteCharacterMovie(graphene.Mutation):
    id = graphene.ID()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id: str) -> "DeleteCharacterMovie":
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
