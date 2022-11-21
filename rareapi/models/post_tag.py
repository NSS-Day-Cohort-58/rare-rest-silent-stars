from django.db import models 

class PostTag(models.Model): 

    post = models.ForeignKey("Post", null=True, blank=True, on_delete =models.CASCADE)
    tag = models.ForeignKey("Tags", null=True, blank=True, on_delete =models.CASCADE)