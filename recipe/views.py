from django.shortcuts import render

from django.http import HttpResponse
from .models import Recipes
import json

def index(request):
    json_open = open('./recipe/fixtures/recipes.json', 'r')
    recipes = json.load(json_open)
    return render(request, 'recipe/card.html', {'recipes': recipes})


def template(request):
    json_open = open('./recipe/fixtures/recipes.json', 'r')
    recipes = json.load(json_open)
    return render(request, 'recipe/test.html', {'recipes': recipes})

def result_sample(request):
    json_open = open('./recipe/fixtures/recipes.json', 'r')
    recipes = json.load(json_open)
    return render(request, 'recipe/result/result-sample.html', {'recipes': recipes})