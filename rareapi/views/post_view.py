from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post

class PostView(ViewSet): 

    def list(self, request): 

        posts = Post.objects.all()
        serialized = PostSerializer(posts, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class PostSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Post
        fields = ('id', 'user', 'tags', 'category', 'title', 'image_url', 'content', 'approved', 'dateTime')