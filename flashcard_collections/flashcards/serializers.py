from rest_framework import serializers
from .models import Flashcard


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['id', 'term', 'definition', 'collection']
