# contentsharing/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('profiles.urls')),
    path('', include('content.urls')),
    path('', include('comment.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
]
