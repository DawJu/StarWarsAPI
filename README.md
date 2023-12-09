This is a simple API that lets you do the basic CRUD operations using GraphQL.
The attached database file contains sample data of some Star Wars characters.

Main technologies used:
- Python 3.12
- Django 4.2.7
- Graphene 3.3
- Graphene-Django 3.1.5
- SQLite3

To run this project:
1. Clone or download this repository and open the project in any IDE.
2. Install libraries listed in `requirements.txt`
3. Run `python manage.py runserver` and click the link. You should land on the app's GraphQL Playground.
4. Here you can use GraphQL to do queries or mutations on the database.

Example queries:
````
query readAll {
  characters {
    edges {
      node {
        characterId
        name
        species
        gender
        age
      }
    }
  }
}
````
````
query helloThere {
  characters(name: "Obi-Wan Kenobi") {
    edges {
      node {
        characterId
        name
        species
        gender
        age
      }
    }
  }
}
````
````
query filter {
  characters(age: 32, gender: OTHER) {
    edges {
      node {
        characterId
        name
        species
        gender
        age
      }
    }
  }
}
````
Example mutations:
````
mutation create {
  createCharacter(name: "test", species: "test", gender: "Male", age: 200) {
    character {
      characterId
      name
      species
      gender
      age
    }
  }
}
````
````
mutation update {
  updateCharacter(characterId: 16, name: "updated name", age: 68) {
    character {
      characterId
      name
      species
      gender
      age
    }
  }
}
````
````
mutation delete {
  deleteCharacter(characterId: 16) {
    characterId
  }
}
````