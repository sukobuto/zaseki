import uuid
from io import BytesIO

from django.db import models
from PIL import Image

# Create your models here.


class Map(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image = models.BinaryField()
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    content_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_image_pil(self):
        return Image.open(BytesIO(self.image))


class Label(models.Model):

    SIZE_LARGE = 'L'
    SIZE_MIDDLE = 'M'
    SIZE_SMALL = 'S'

    CHOICES_FOR_SIZE = (
        (SIZE_LARGE, '大'),
        (SIZE_MIDDLE, '中'),
        (SIZE_SMALL, '小'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='labels')
    x = models.IntegerField()
    y = models.IntegerField()
    text = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=1, choices=CHOICES_FOR_SIZE, default=SIZE_MIDDLE)
