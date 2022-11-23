from django.db import models
from django.contrib.auth.models import User


class RareUser(models.Model): 

    user= models.ForeignKey(User, on_delete =models.CASCADE)
    bio = models.CharField(max_length=24)
    profile_image = models.CharField(max_length=400)