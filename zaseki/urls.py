"""zaseki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from map.views import index, MapUploadView, map_image, MapViewSet, LabelViewSet

router = SimpleRouter()
router.register('maps', MapViewSet)
router.register('labels', LabelViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/upload-map/', MapUploadView.as_view()),
    path('image/map/<uuid:map_id>.jpg', map_image),
    path('image/map/<uuid:map_id>.png', map_image),
]
