#!/usr/bin/env python3

import json
import uuid

root = []

#with open("./recipe/fixtures/recipes.json", encoding='unicode-escape') as f:
with open("./recipe/fixtures/recipes.json") as f:
    for recipe in json.load(f):
        #print(recipe)
        recipes_id = str(uuid.uuid4())
        root.append({
            "model": "recipe.recipes",
            "pk": recipes_id,
            "fields": {
                "title": recipe["title"], 
                "url": recipe["url"],
                "thumbnail_url": recipe["thumbnail_url"],
            }
        })
        for tag in recipe["tags"]:
            #print(tag)
            root.append({
                "model": "recipe.tags",
                "pk": str(uuid.uuid4()),
                "fields": {
                    "name": tag,
                    "recipes_id": recipes_id,
                    "material_type": 1,
                }
            })

print(json.dumps(root,ensure_ascii=False))
