from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model): 
    author = models.OneToOneField('RareUser', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', null=True, blank=True, on_delete =models.CASCADE)
    content = models.CharField(max_length=300)
