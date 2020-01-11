#!/usr/bin/env python
# -*- coding: utf-8 -*-

from easygraphql import GraphQL
import json

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
print(json.dumps(result, indent=4))