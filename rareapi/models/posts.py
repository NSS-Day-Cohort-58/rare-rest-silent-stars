from django.db import models
from django.contrib.auth.models import User

class Post(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tags =  models.ManyToManyField("Tags", through="PostTags")
    category = models.ForeignKey("Category", null=True, blank=True, on_delete =models.CASCADE)
    title = models.CharField(max_length=24)
    image_url = models.CharField()
    content = models.CharField()
    approved = models.BooleanField()
    dateTime = models.DateTimeField()