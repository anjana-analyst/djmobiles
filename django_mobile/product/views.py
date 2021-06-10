from django.http import Http404
from rest_framework import response
from .models import Category, Product
from .serializers import ProductSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class LatestProductsList(APIView):
    def get(self,request,format=None):
        products= Product.objects.all()[0:2]
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self,category_slug,product_slug):
        try:
            return Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self,request,category_slug,product_slug,format=None):
        product=self.get_object(category_slug,product_slug)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self,category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self,request,category_slug,format=None):
        category=self.get_object(category_slug)
        serializer= CategorySerializer(category)
        return Response(serializer.data)