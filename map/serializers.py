from rest_framework import serializers
from .models import Map, Label


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = (
            'id',
            'name',
            'content_type',
            'width',
            'height',
            'created_at',
            'updated_at',
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['image_url'] = instance.image_url
        return ret


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
