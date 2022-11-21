from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category

class CategoryView(ViewSet):

    def create(self, request):

        category = Category.objects.create(
            label=request.data["label"]
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'label') 