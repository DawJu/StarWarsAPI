from StarWars.models import Character


class CharacterService:
    @staticmethod
    def create_character(name, gender, age, species=None):
        character = Character(name=name, species=species, gender=gender, age=age)
        character.save()
        return character

    @staticmethod
    def update_character(id, **kwargs):
        character = Character.objects.get(pk=id)
        if 'name' in kwargs:
            character.name = kwargs['name']
        if 'species' in kwargs:
            character.species = kwargs['species']
        if 'gender' in kwargs:
            character.gender = kwargs['gender']
        if 'age' in kwargs:
            character.age = kwargs['age']
        character.save()
        return character

    @staticmethod
    def delete_character(id):
        character = Character.objects.get(pk=id)
        character.delete()
