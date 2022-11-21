from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, Category

class PostView(ViewSet): 

    def list(self, request): 

        posts = Post.objects.all()
        serialized = PostSerializer(posts, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def update(self, request, pk): 

        post = Post.objects.get(pk=pk)
        post.user = User.objects.get(pk=request.data["user"])
        post.tags = Tag.objects.get(pk=request.data["tag"])
        post.category = Category.objects.get(pk=request.data["category"])
        post.title = request.data["title"]
        post.image_url = request.data["image_url"]
        post.content = request.data["content"]
        post.approved = request.data["approved"]
        post.publication_date = request.data["publication_date"]
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)




class PostSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Post
        fields = ('id', 'user', 'tags', 'category', 'title', 'image_url', 'content', 'approved', 'publication_date')