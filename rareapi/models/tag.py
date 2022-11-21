from django.db import models

class Tag(models.model): 
    label = models.CharField(max_length=30)
    