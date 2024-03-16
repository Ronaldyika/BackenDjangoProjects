from django.db import models
class Profile(models.Model):
    name = models.CharField(max_length = 45)
    email = models.EmailField(max_length= 45)
    image = models.ForeignKey('Image',on_delete=models.CASCADE)


class Image(models.Model):
    image = models.ImageField(upload_to='static/profile')

class Project(models.Model):
    urllink = models.URLField()
    image = models.ImageField(upload_to='static/projects')