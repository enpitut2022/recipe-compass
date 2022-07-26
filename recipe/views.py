from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("注文の多い料理店：recipe-compass")