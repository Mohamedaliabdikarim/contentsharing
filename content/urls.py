# content/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'contents', ContentViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('content', include(router.urls)),
]
