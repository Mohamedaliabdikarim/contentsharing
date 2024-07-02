from rest_framework import serializers
from .models import Content, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ContentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    categories = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Category.objects.all()
    )
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    image = serializers.ImageField(required=False, allow_null=True)

    def validate_image(self, value):
        if value and value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value and value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        if value and value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    class Meta:
        model = Content
        fields = ['id', 'title', 'text', 'owner', 'is_owner','created_at', 'updated_at', 'categories', 'image', 'profile_id', 'profile_image']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        text = Content.objects.create(**validated_data)
        for category_name in categories_data:
            category = Category.objects.get(name=category_name)
            text.categories.add(category)
        return text
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
