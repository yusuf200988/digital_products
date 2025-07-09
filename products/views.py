from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, File, Product
from .serializers import CategorySerializer, FileSerializer, ProductSerializer


class CategoryListView(APIView):

    def get(self, req):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': req})
        return Response(serializer.data)
    

class CategoryDetailView(APIView):

    def get(self, req, id):
        category = get_object_or_404(Category, pk=id)
        serializer = CategorySerializer(category, context={'request': req})
        return Response(serializer.data)


class ProductListView(APIView):

    def get(self, req):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': req})
        return Response(serializer.data)
    

class ProductDetailView(APIView):
    
    def get(self, req, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, context={'request': req})
        return Response(serializer.data)
    

class FileListView(APIView):

    def get(self, req, product_id):
        files = get_list_or_404(File, pk=product_id)
        serializer = FileSerializer(files, many=True, context={'request': req})
        return Response(serializer.data)
    

class FileDetailView(APIView):

    def get(self, req, product_id, id):
        file = get_object_or_404(File, product_id=product_id, pk=id)
        serializer = FileSerializer(file, context={'request': req})
        return Response(serializer.data)