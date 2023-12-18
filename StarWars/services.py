from graphql_relay.node.node import from_global_id

from StarWars.models import Character, CharacterMovie, Movie


class CharacterService:
    @staticmethod
    def create_character(name: str, gender: str, age: int, species: str | None = None) -> Character:
        character = Character(name=name, species=species, gender=gender, age=age)
        character.save()
        return character

    @staticmethod
    def update_character(id: int, **kwargs) -> Character:
        character = Character.objects.get(pk=id)
        if "name" in kwargs:
            character.name = kwargs["name"]
        if "species" in kwargs:
            character.species = kwargs["species"]
        if "gender" in kwargs:
            character.gender = kwargs["gender"]
        if "age" in kwargs:
            character.age = kwargs["age"]
        character.save()
        return character

    @staticmethod
    def delete_character(id: int) -> None:
        character = Character.objects.get(pk=id)
        character.delete()


class MovieService:
    @staticmethod
    def create_movie(name: str, episode: int | None = None, release_year: int | None = None) -> Movie:
        movie = Movie(name=name, episode=episode, release_year=release_year)
        movie.save()
        return movie

    @staticmethod
    def update_movie(id: int, **kwargs) -> Movie:
        movie = Movie.objects.get(pk=id)
        if "name" in kwargs:
            movie.name = kwargs["name"]
        if "episode" in kwargs:
            movie.episode = kwargs["episode"]
        if "release_year" in kwargs:
            movie.release_year = kwargs["release_year"]
        movie.save()
        return movie

    @staticmethod
    def delete_movie(id: int) -> None:
        movie = Movie.objects.get(pk=id)
        movie.delete()


class CharacterMovieService:
    @staticmethod
    def create_character_movie(**kwargs) -> CharacterMovie:
        if "character_name" not in kwargs and "character_id" not in kwargs:
            return None
        if (
            "movie_name" not in kwargs
            and "movie_episode" not in kwargs
            and "movie_id" not in kwargs
        ):
            return None
        if "character_name" in kwargs:
            character = Character.objects.get(name__iexact=kwargs["character_name"])
        else:
            character_id = from_global_id("character_id")[1]
            character = Character.objects.get(pk=character_id)
        if "movie_name" in kwargs:
            movie = Movie.objects.get(name__iexact=kwargs["movie_name"])
        elif "movie_episode" in kwargs:
            movie = Movie.objects.get(episode=kwargs["movie_episode"])
        else:
            movie_id = from_global_id("movie_id")[1]
            movie = Movie.objects.get(pk=movie_id)
        if CharacterMovie.objects.filter(character=character, movie=movie).exists():
            return None
        character_movie = CharacterMovie(character=character, movie=movie)
        character_movie.save()
        return character_movie

    @staticmethod
    def delete_character_movie(id: int) -> None:
        character_movie = CharacterMovie.objects.get(pk=id)
        character_movie.delete()
