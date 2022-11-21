from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Tag

class TagView(ViewSet): 

    def create(self, request): 

        tag = Tag.objects.create(
            label = request.data["label"]
        )

        serializer = TagSerializer(tag)
        return Response(serializer.data)

class TagSerializer(serializers.ModelSerializer):

    model = Tag
    fields = ('id', 'label')
    