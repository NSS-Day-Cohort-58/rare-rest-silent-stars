from django.db import models
from django.contrib.auth.models import User


class RareUser(models.Model): 

    bio = models.CharField(max_length=24)
    profile_image = models.CharField(max_length=400)
    user= models.ForeignKey(User, on_delete =models.CASCADE)