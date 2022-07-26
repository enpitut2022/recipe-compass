from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from django.db import models
import uuid

# Create your models here.
class Recipes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    thumbnail_url = models.URLField()
    title = models.CharField(max_length=128)

class Tags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipes_id = models.ForeignKey(
        'Recipes',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=128)
    material_type = models.PositiveSmallIntegerField()