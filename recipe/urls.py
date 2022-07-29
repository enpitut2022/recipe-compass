from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('template', views.template, name="template"),
    path('result', views.result, name="result_sample"),
]