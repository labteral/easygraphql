#!/usr/bin/env python
# -*- coding: utf-8 -*-

from easygraphql import GraphQL
import json

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
print(json.dumps(result, indent=4))