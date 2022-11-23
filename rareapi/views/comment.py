from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment, RareUser, Post

class CommentView(ViewSet):

    def list(self, request): 

        comments = Comment.objects.all()
        serialized = CommentSerializer(comments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):

        author = RareUser.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=request.data[postId])
        
        category = Comment.objects.create(
            content=request.data["content"],
            author=author,
            post=post
        )
        serializer = CommentSerializer(category)
        return Response(serializer.data)

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'content') 

