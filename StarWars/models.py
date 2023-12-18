from django.db import models

# Create your models here.


class Character(models.Model):
    character_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50, verbose_name="Name")
    species = models.TextField(max_length=15, null=True, verbose_name="Species")

    class Gender(models.TextChoices):
        Male = "Male"
        Female = "Female"
        Other = "Other"

    gender = models.TextField(
        max_length=6, choices=Gender.choices, verbose_name="Gender"
    )
    age = models.IntegerField(verbose_name="Age")

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self):
        return f"{self.name} ({self.character_id})"


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, verbose_name="Name")
    episode = models.IntegerField(null=True, verbose_name="Episode")
    release_year = models.IntegerField(null=True, verbose_name="Release Year")

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"Episode {self.episode} - {self.name} ({self.release_year})"


class CharacterMovie(models.Model):
    character_movie_id = models.AutoField(primary_key=True)
    character = models.ForeignKey(Character,
                                  on_delete=models.CASCADE,
                                  related_name="characters",
                                  related_query_name="character"
                                  )
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name="movies",
                              related_query_name="movie"
                              )

    class Meta:
        verbose_name = "Character + Movie"
        verbose_name_plural = "Characters + Movies"

    def __str__(self):
        return f"{self.character.name} from {self.movie.name} ({self.character_movie_id})"
