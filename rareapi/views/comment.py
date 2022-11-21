from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment

class CoomentView(ViewSet):

    def create(self, request):

        category = Comment.objects.create(
            label=request.data["label"]
        )
        serializer = CommentSerializer(category)
        return Response(serializer.data)

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'label') 