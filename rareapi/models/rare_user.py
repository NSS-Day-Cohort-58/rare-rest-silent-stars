from django.db import models


class RareUser(models.Model): 

    bio = models.CharField(max_length=24)
    profile_image = models.CharField()
    user= models.ForeignKey("User", on_delete =models.CASCADE)