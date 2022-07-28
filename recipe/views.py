from django.shortcuts import render

from django.http import HttpResponse
from .models import Recipes, Tags
import json


def index(request):
    json_open = open('./recipe/fixtures/recipes.json', 'r', encoding="utf-8")
    recipes = json.load(json_open, encoding="utf-8")
    return render(request, 'recipe/card.html', {'recipes': recipes})

# dbtest
def template(request):
    recipes = []
    for data in Recipes.objects.all().values('id'):
        recipe = dict()
        uuid = str(data['id']).replace('-', '')
        recipe['title'] = Recipes.objects.filter(id=uuid).first().title
        recipe['url'] = Recipes.objects.filter(id=uuid).first().url
        recipe['thumbnail_url'] = Recipes.objects.filter(id=uuid).first().thumbnail_url
        tag = []
        for i in Tags.objects.filter(recipes_id=uuid).all():
            #print(i)
            tag.append(i.name)
        recipe['tags'] = tag
        recipes.append(recipe)
    return render(request, 'recipe/card.html', {'recipes': recipes})

def result_sample(request):
    json_open = open('./recipe/fixtures/recipes.json', 'r', encoding="utf-8")
    recipes = json.load(json_open)
    return render(request, 'recipe/result/result-sample.html', {'recipes': recipes})