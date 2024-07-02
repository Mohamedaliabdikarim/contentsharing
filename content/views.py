from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Content, Category
from .serializers import ContentSerializer, CategorySerializer
from contentsharing.permissions import IsOwnerOrReadOnly

class ContentList(APIView):
    """
    List content or create content if logged in
    """
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        contents = Content.objects.all()
        serializer = ContentSerializer(
            contents, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ContentSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class ContentDetail(APIView):
    """
    Retrieve a content item and edit or delete it if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContentSerializer

    def get_object(self, pk):
        try:
            content = Content.objects.get(pk=pk)
            self.check_object_permissions(self.request, content)
            return content
        except Content.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        text = self.get_object(pk)
        serializer = ContentSerializer(
            text, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        text = self.get_object(pk)
        serializer = ContentSerializer(
            text, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        text = self.get_object(pk)
        text.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

class CategoryList(APIView):
    """
    List categories or create a category if logged in
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(
            categories, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class CategoryDetail(APIView):
    """
    Retrieve a category and edit or delete it if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            self.check_object_permissions(self.request, category)
            return category
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(
            category, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(
            category, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
