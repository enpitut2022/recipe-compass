from django.shortcuts import render

from django.http import HttpResponse
from .models import Recipes
import json

def index(request):
    recipes = Recipes.objects.all()[:5]
    s ="<!doctype html><html><body>"
    for i in recipes:
        s += f"<section>"
        s += f'<a href="{i.url}">{i.title}</p>'
        s += f"<section>"
    s += "</body></html>"
    return HttpResponse(s)

def view_json(request):
    json_open = open('../fixtures/recipes.json', 'r')
    recipes = json.load(json_open)
    return render(request, 'view_json.html', {'recipes': recipes})

def template(request):
    return render(request, 'recipe/test.html')