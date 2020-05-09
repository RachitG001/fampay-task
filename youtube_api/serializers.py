from rest_framework import serializers
from .models import Cricket


class CricketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cricket
        exclude = ('id',)

    # def run_validators(self, value):
    #     for validator in self.validators:
    #         if isinstance(validator, validators.UniqueTogetherValidator):
    #             self.validators.remove(validator)
    #     super(CricketSerializer, self).run_validators(value)

    def get_or_create(self):
        defaults = self.validated_data.copy()
        identifier = defaults.pop('videoId')
        return Cricket.objects.get_or_create(videoId=identifier, defaults=defaults)