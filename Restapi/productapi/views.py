from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.decorators import action
from rest_framework.response import  Response
from rest_framework.parsers import FormParser,MultiPartParser,JSONParser
from .serializers import ProductSerializer
from .models import Product
from rest_framework import status
class ProductListView (APIView):

      def get(self,request):
          products=Product.objects.all ()
          serializer = ProductSerializer(products,many=True)
          return Response(serializer.data)
      def post(self,request):
          serializer=ProductSerializer(data=request.data)
          if (serializer.is_valid()):
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView (APIView):

 #   parser_classes=(FormParser, MultiPartParser, JSONParser)
    def get(self,request, call):
       product=Product.objects.get(id=call)
       serializer = ProductSerializer(product)
       return Response(serializer.data)
#
    def put(self,request, call):
        product=Product.objects.get(id=call)
        serializer = ProductSerializer(product, data=request.data )
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request, call=None):
        product=Product.objects.get(id=call)
        product.delete()
        return Response(status=status.HTTP_200_OK)