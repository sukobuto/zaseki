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


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
