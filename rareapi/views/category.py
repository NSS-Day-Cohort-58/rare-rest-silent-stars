from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category

class CategoryView(ViewSet):

    def list(self, request):
        """Handle GET requests to get all the categories
        Returns:
            Response -- JSON serialized list all the categories
        """
        categories = Category.objects.all().order_by('label').values()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    
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