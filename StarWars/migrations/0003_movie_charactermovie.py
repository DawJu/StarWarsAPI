# Generated by Django 4.2.7 on 2023-12-18 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("StarWars", "0002_alter_character_species"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("movie_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField(max_length=100, verbose_name="Name")),
                ("episode", models.IntegerField(verbose_name="Episode")),
                ("release_year", models.IntegerField(verbose_name="Release Year")),
            ],
            options={
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
            },
        ),
        migrations.CreateModel(
            name="CharacterMovie",
            fields=[
                (
                    "character_movie_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "character",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="StarWars.character",
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="StarWars.movie"
                    ),
                ),
            ],
            options={
                "verbose_name": "Character + Movie",
                "verbose_name_plural": "Characters + Movies",
            },
        ),
    ]
