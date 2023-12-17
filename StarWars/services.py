from StarWars.models import Character


class CharacterService:
    @staticmethod
    def create_character(name, gender, age, species=None):
        character = Character(name=name, species=species, gender=gender, age=age)
        character.save()
        return character

    @staticmethod
    def update_character(character_id, **kwargs):
        character = Character.objects.get(character_id=character_id)
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
    def delete_character(character_id):
        character = Character.objects.get(character_id=character_id)
        character.delete()
        return character_id
