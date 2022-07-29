from django.shortcuts import render

from django.http import HttpResponse
from .models import Recipes, Tags
import json


def index(request):
    json_open = open('./recipe/fixtures/recipes.json', 'r', encoding="utf-8")
    recipes = json.load(json_open)
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
            tag.append(i.name)
        recipe['tags'] = tag
        recipes.append(recipe)
    return render(request, 'recipe/card.html', {'recipes': recipes})


# GETで送られた値の受け取り
def result(request):
    queries = request.GET.get("search")
    query_not = request.GET.get("not-search")
    recipes = []
    recipes_num = {}
    queries_list = queries.split()
    #excluded_list = Tags.objects.exclude(name__in=queries_not_list).all()

    for query in queries_list:
        filtered_recipes = Tags.objects.filter(name=query).all()

        # if not len(excluded_list) == 0:
        #     filtered_recipes = filtered_recipes.intersection(excluded_list)
        #     print(f"filtered_recipes: {filtered_recipes}")
        #     print(f"excluded_list: {excluded_list}")

        for data in filtered_recipes:
            uuid = str(data.recipes_id).replace('-', '').split('(')[1].split(')')[0]
            if uuid in list(recipes_num.keys()):
            #if uuid in recipes_num:
                recipes_num[uuid] = recipes_num[uuid] + 1
            else:
                recipes_num[uuid] = 1

    queries_not_list = query_not.split()
    
    for query_not in queries_not_list:
        for data in Tags.objects.filter(name=query_not).all():
            uuid = str(data.recipes_id).replace('-', '').split('(')[1].split(')')[0]
            if uuid in list(recipes_num.keys()):
            #if uuid in recipes_num:
                recipes_num[uuid] = recipes_num[uuid] - 1
            else:
                recipes_num[uuid] = -1

    for key, value in recipes_num.items():
        if value == len(queries_list):
            recipe = dict()
            recipe['title'] = Recipes.objects.filter(id=key).first().title
            #print(recipe['title'])
            recipe['url'] = Recipes.objects.filter(id=key).first().url
            recipe['thumbnail_url'] = Recipes.objects.filter(id=key).first().thumbnail_url
            tag = []
            for i in Tags.objects.filter(recipes_id=key).all():
                tag.append(i.name)
            recipe['tags'] = tag
            recipes.append(recipe)
    
    #for data in Tags.objects.filter(name__in=query).all():
        #uuid = str(data.recipes_id).replace('-', '').split('(')[1].split(')')[0]
        #print('\n\n\n\n');print(uuid);print('\n\n\n\n')

    #print(recipes)
    return render(request, 'recipe/result/result-sample.html', {'recipes': recipes, 'query': queries_list, 'query_not': queries_not_list})

def result_sample(request):
    json_open = open('./recipe/fixtures/recipes.json', 'r', encoding="utf-8")
    recipes = json.load(json_open)
    return render(request, 'recipe/result/result-sample.html', {'recipes': recipes})