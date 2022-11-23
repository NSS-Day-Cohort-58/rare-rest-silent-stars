from django.db import models

class Post(models.Model):
    user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    tags =  models.ManyToManyField("Tag", through="PostTag")
    category = models.ForeignKey("Category", null=True, blank=True, on_delete =models.CASCADE)
    title = models.CharField(max_length=24)
    image_url = models.CharField(max_length=400)
    content = models.CharField(max_length=200)
    approved = models.BooleanField()
    publication_date = models.DateField()