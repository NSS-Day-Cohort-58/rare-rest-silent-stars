from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Tag

class TagView(ViewSet):

    def list(self, request):

        tag = Tag.objects.all().order_by('label').values()
        serialized = TagSerializer(tag, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


    def create(self, request): 

        tag = Tag.objects.create(
            label = request.data["label"]
        )

        serializer = TagSerializer(tag)
        return Response(serializer.data)


    def destroy(self, request, pk): 

        tag = Tag.objects.get(pk=pk)
        tag.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

        

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'label')
    