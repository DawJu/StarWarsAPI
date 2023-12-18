from StarWars.models import Character, Movie, CharacterMovie


class CharacterService:
    @staticmethod
    def create_character(name, gender, age, species=None):
        character = Character(name=name, species=species, gender=gender, age=age)
        character.save()
        return character

    @staticmethod
    def update_character(id, **kwargs):
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
    def delete_character(id):
        character = Character.objects.get(pk=id)
        character.delete()


class MovieService:
    @staticmethod
    def create_movie(name, episode=None, release_year=None):
        movie = Movie(name=name, episode=episode, release_year=release_year)
        movie.save()
        return movie

    @staticmethod
    def update_movie(id, **kwargs):
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
    def delete_movie(id):
        movie = Movie.objects.get(pk=id)
        movie.delete()


class CharacterMovieService:
    @staticmethod
    def create_character_movie(character_id, movie_id):
        character_movie = CharacterMovie(
            character=Character.objects.get(pk=character_id),
            movie=Movie.objects.get(pk=movie_id)
        )
        character_movie.save()
        return character_movie

    @staticmethod
    def delete_character_movie(id):
        character_movie = CharacterMovie.objects.get(pk=id)
        character_movie.delete()
