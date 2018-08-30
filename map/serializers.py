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
        v = instance.updated_at.strftime('%Y%m%d%H%M%S%f%Z')
        ret['image_url'] = instance.image_url + f'?v={v}'
        return ret


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
