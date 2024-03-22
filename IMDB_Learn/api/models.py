from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    isActive = models.BooleanField(default= False)

    def __init__(self):
        return self.name