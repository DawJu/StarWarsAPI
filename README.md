This is a simple API that lets you do the basic CRUD operations using GraphQL.
The attached database file contains sample data of some Star Wars characters and movies.
The app has 3 models: Character, Movie and CharacterMovie (stores information of a character being in a movie).

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
query allChar {
  characters {
    edges {
      node {
        id
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
  characters(name_Icontains: "kenobi") {
    edges {
      node {
        id
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
query allMov {
  movies {
    edges {
      node {
        id
        name
        episode
        releaseYear
      }
    }
  }
}
````
````
query filterCharMov {
  characterMovies(movieName: "empire") {
    edges {
      node {
        id
        character {
          name
        }
        movie {
          name
        }
      }
    }
  }
}
````
Example mutations:
````
mutation createChar {
  createCharacter(name: "test", gender: "Male", age: 40) {
    character {
      id
      name
      species
      gender
      age
    }
  }
}
````
````
mutation updateMov {
  updateMovie(id: "TW92aWVOb2RlOjM=", releaseYear: 2024) {
    movie {
      id
      name
      episode
      releaseYear
    }
  }
}
````
````
mutation deleteCharMov {
  deleteCharacterMovie(id: "Q2hhcmFjdGVyTW92aWVOb2RlOjU=") {
    id
  }
}
````