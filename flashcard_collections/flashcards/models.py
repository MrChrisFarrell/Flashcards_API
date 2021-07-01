from django.db import models

class Flashcard(models.Model):
    term = models.CharField(max_length=50)
    definition = models.CharField(max_length=150)
    collection = models.IntegerField(default=0)
