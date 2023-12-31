# Generated by Django 4.2.7 on 2023-12-18 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("StarWars", "0005_alter_movie_episode_alter_movie_release_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="name",
            field=models.TextField(max_length=50, unique=True, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="charactermovie",
            name="character",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="characters",
                related_query_name="character",
                to="StarWars.character",
                verbose_name="Character",
            ),
        ),
        migrations.AlterField(
            model_name="charactermovie",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movies",
                related_query_name="movie",
                to="StarWars.movie",
                verbose_name="Movie",
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="episode",
            field=models.IntegerField(null=True, unique=True, verbose_name="Episode"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="name",
            field=models.TextField(max_length=100, unique=True, verbose_name="Name"),
        ),
    ]
