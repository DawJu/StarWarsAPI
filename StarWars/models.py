from django.db import models

# Create your models here.


class Character(models.Model):
    character_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50, verbose_name='Name')
    species = models.TextField(max_length=15, verbose_name='Species')

    class Gender(models.TextChoices):
        Male = 'Male'
        Female = 'Female'
        Other = 'Other'

    gender = models.TextField(max_length=6, choices=Gender.choices, verbose_name='Gender')
    age = models.IntegerField(verbose_name='Age')

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'

    def __str__(self):
        return f'{self.name} ({self.character_id})'
