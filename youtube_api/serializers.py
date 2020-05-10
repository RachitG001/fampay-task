from rest_framework import serializers
from .models import Cricket


class CricketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cricket
        exclude = ('id',)
        validators = []


    def create(self, validated_data):
        item, created = Cricket.objects.get_or_create(
            videoId=validated_data.get('videoId'),
            defaults=validated_data
        )
        return item