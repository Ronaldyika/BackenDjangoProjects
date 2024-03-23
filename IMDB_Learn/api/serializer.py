from rest_framework import serializers
from .models import Watchlist,StreamPlateform

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = '__all__'

        # def validate_name(self,value):
        #     if len(value)< 2:
        #         raise serializers.ValidationError("name should be longer than "+ value)
        #     else:
        #         return value


class StreamPlateformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True,read_only=True)
    class Meta:
        model = StreamPlateform
        fields = '__all__'