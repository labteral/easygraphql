# easygraphql
A minimal library to interact with GraphQL from Python

## Installation
```bash
pip install easygraphql
```

## Usage

### Instantiation
```python
from easygraphql import GraphQL

graphql = GraphQL('https://example.org/graphql')
query = '''
    query {
        hello
    }
'''
result = graphql.execute(query)
```

### Authentication
You can set global headers that will be added to all your GraphQL operations: 
```python
graphql.set_headers({'Authorization': 'Bearer xxxxx'})
```

You can also unset them:
```python
graphql.unset_headers()
```

Or directly provide them on every execution:
```python
result = graphql.execute(query, headers={'Authorization': 'Bearer xxxxx'})
```

## Examples

### Query without variables
```python
from easygraphql import GraphQL

graphql = GraphQL('https://swapi-graphql.netlify.com/.netlify/functions/index')
query = '''
    query {
        allFilms {
            films {
                title
                director
            }
        }
    }
'''
result = graphql.execute(query)
```

```json
{
    "allFilms": {
        "films": [
            {
                "title": "A New Hope",
                "director": "George Lucas"
            },
            {
                "title": "The Empire Strikes Back",
                "director": "Irvin Kershner"
            },
            {
                "title": "Return of the Jedi",
                "director": "Richard Marquand"
            },
            {
                "title": "The Phantom Menace",
                "director": "George Lucas"
            },
            {
                "title": "Attack of the Clones",
                "director": "George Lucas"
            },
            {
                "title": "Revenge of the Sith",
                "director": "George Lucas"
            },
            {
                "title": "The Force Awakens",
                "director": "J. J. Abrams"
            }
        ]
    }
}
```

### Query with variables
```python
from easygraphql import GraphQL

graphql = GraphQL('https://swapi-graphql.netlify.com/.netlify/functions/index')
query = '''
    query GetFilm($id: ID!){
        film(id: $id) {
            title
            director
        }
    }
'''
variables = {"id": "ZmlsbXM6MQ=="}
result = graphql.execute(query, variables)
```

```json
{
    "film": {
        "title": "A New Hope",
        "director": "George Lucas"
    }
}
```
