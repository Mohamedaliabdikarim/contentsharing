# content/serializers.py

from rest_framework import serializers
from .models import Content, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ContentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    categories = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Category.objects.all()
    )
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'author', 'created_at', 'updated_at', 'categories', 'image']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        content = Content.objects.create(**validated_data)
        for category_name in categories_data:
            category = Category.objects.get(name=category_name)
            content.categories.add(category)
        return content
