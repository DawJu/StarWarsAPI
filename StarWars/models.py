from django.db import models
from django.db.models import (AutoField, ForeignKey, IntegerField, TextChoices,
                              TextField)

# Create your models here.


class Character(models.Model):
    character_id: AutoField = AutoField(primary_key=True)
    name: TextField = TextField(max_length=50, unique=True, verbose_name="Name")
    species: TextField = TextField(max_length=15, null=True, verbose_name="Species")

    class Gender(TextChoices):
        Male = "Male"
        Female = "Female"
        Other = "Other"

    gender: TextField = TextField(
        max_length=6, choices=Gender.choices, verbose_name="Gender"
    )
    age: IntegerField = IntegerField(verbose_name="Age")

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self) -> str:
        return f"{self.name} ({self.character_id})"


class Movie(models.Model):
    movie_id: AutoField = AutoField(primary_key=True)
    name: TextField = TextField(max_length=100, unique=True, verbose_name="Name")
    episode: IntegerField = IntegerField(null=True, unique=True, verbose_name="Episode")
    release_year: IntegerField = IntegerField(null=True, verbose_name="Release Year")

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self) -> str:
        return f"Episode {self.episode} - {self.name} ({self.release_year})"


class CharacterMovie(models.Model):
    character_movie_id: AutoField = AutoField(primary_key=True)
    character: ForeignKey = ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name="characters",
        related_query_name="character",
        verbose_name="Character",
    )
    movie: ForeignKey = ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="movies",
        related_query_name="movie",
        verbose_name="Movie",
    )

    class Meta:
        verbose_name = "Character + Movie"
        verbose_name_plural = "Characters + Movies"

    def __str__(self) -> str:
        return (
            f"{self.character.name} from {self.movie.name} ({self.character_movie_id})"
        )
