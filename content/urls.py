from django.urls import path
from . import views

urlpatterns = [
    path('contents/', views.ContentList.as_view(), name='ContentLis'),
    path('contents/<int:pk>/', views.ContentDetail.as_view(), name='content-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
]