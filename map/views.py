from io import BytesIO

from PIL import Image
from basicauth.decorators import basic_auth_required
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import Map, Label
from .serializers import MapSerializer, LabelSerializer

# Create your views here.


@basic_auth_required
def index(request):
    return render(request, 'index.html', {})


class MapUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    renderer_classes = (JSONRenderer,)

    def post(self, request, format=None):
        image_file: InMemoryUploadedFile = request.data['image']
        name = request.data['name']
        image_bytes = image_file.read()
        image: Image = Image.open(BytesIO(image_bytes))
        map = Map(
            name=name,
            image=image_bytes,
            content_type=image_file.content_type,
            width=image.width,
            height=image.height
        )
        map.save()
        return Response(MapSerializer(map).data, status=201)


def map_image(request, map_id):
    map = get_object_or_404(Map, pk=map_id)
    ims = request.META.get('HTTP_IF_MODIFIED_SINCE', None)
    if ims is not None and ims >= map.updated_at.strftime('%a, %d %b %Y %H:%M:%S GMT'):
        return HttpResponse(status=304)
    image_bytes = map.image
    response = HttpResponse(image_bytes, content_type=map.content_type)
    response['Content-Length'] = len(image_bytes)
    response['Cache-Control'] = "max-age=0"
    response['Last-Modified'] = map.updated_at.strftime('%a, %d %b %Y %H:%M:%S GMT')
    return response


class MapViewSet(ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    ordering_fields = '__all__'

    @action(methods=['put'], detail=True)
    def change_image(self, request, pk=None):
        map = get_object_or_404(Map, pk=pk)
        image_file: InMemoryUploadedFile = request.data['image']
        image_bytes = image_file.read()
        image: Image = Image.open(BytesIO(image_bytes))
        map.image = image_bytes
        map.content_type = image_file.content_type
        map.width = image.width
        map.height = image.height
        map.save()
        return Response(MapSerializer(map).data, status=200)


class LabelViewSet(ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    filter_fields = ('map_id', 'size')
    ordering_fields = '__all__'
