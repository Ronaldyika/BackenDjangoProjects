from django.db import models

class StreamPlateform(models.Model):
    name = models.CharField(max_length=30)
    urlpath = models.URLField()
    date_updated = models.DateTimeField(auto_now_add = True)

class Watchlist(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    plateform = models.ForeignKey("StreamPlateform",on_delete=models.CASCADE,related_name = 'watchlist')
    isActive = models.BooleanField(default= False)
    date_created = models.DateField(auto_now_add = True)

    def create(self,validated_data):
        return Watchlist.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.isActive = validated_data.get('isActive',instance.isActive)

        instance.save()
        return instance
