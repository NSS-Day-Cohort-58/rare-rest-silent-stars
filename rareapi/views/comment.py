from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment

class CommentView(ViewSet):

    def create(self, request):

        author = User.objects.get(user=request.auth.user)
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
        fields = ('id', 'user', 'post', 'content') 

