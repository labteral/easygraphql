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
data, errors = graphql.execute(query, variables)
print(json.dumps(data, indent=4))