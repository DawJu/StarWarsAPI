import json

from django.test import TransactionTestCase
from graphene_django.utils.testing import GraphQLTestCase  # type: ignore

from StarWars.models import Character
from StarWars.services import CharacterService

# Create your tests here.


class StarWarsTestCase(GraphQLTestCase):
    GRAPHQL_URL: str = "http://localhost/"

    def setUp(self) -> None:
        Character.objects.create(
            name="Test Character", species="Human", gender="Male", age=18
        )

    def test_show_characters_query(self) -> None:
        response = self.query(
            """
            query {
              characters {
                edges {
                  node {
                    id
                    name
                  }
                }
              }
            }
            """
        )

        content = json.loads(response.content)

        self.assertResponseNoErrors(response)

    def test_create_character_mutation(self) -> None:
        response = self.query(
            """
            mutation {
              createCharacter(name: "Test Character Create", gender: "Male", age: 40) {
                character {
                  id
                  name
                  species
                  gender
                  age
                }
              }
            }
            """
        )
        test_char = Character.objects.get(name="Test Character Create")

        content = json.loads(response.content)

        self.assertResponseNoErrors(response)
        self.assertEqual(test_char.age, 40)


class CharacterModelTestCase(TransactionTestCase):
    def setUp(self) -> None:
        Character.objects.create(
            name="Char for removal", species="Unknown", gender="Other", age=9
        )

    def test_delete_character(self) -> None:
        test_char = Character.objects.get(name="Char for removal")
        id = test_char.character_id
        CharacterService().delete_character(id)

        with self.assertRaises(Character.DoesNotExist):
            Character.objects.get(pk=id)
