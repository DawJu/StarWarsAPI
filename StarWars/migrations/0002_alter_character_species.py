# Generated by Django 4.2.7 on 2023-12-16 22:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("StarWars", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="species",
            field=models.TextField(max_length=15, null=True, verbose_name="Species"),
        ),
    ]
