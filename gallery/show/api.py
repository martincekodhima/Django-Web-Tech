from .models import Image
from .serializers import ImageSerializer, ImageDetailSerializer
from django.http import Http404
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64
from django.core.files.base import ContentFile

class PhotoList(APIView):
            
    def get(self, request):
        images = Image.objects.all()
        serializedImages = ImageSerializer(images, many=True)
        return Response(serializedImages.data)
    
    def put(self,request):
        serializer = ImageDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PhotoDetail(APIView):
    def get_objects(self,pk):
        try:
            return Image.objects.get(id=pk) 
        except Image.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        images = self.get_objects(pk)
        serializedImages = ImageDetailSerializer(images)
        return Response(serializedImages.data)
        
    def delete(self, request, pk):
        images = self.get_objects(pk)
        images.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, pk):
        images = self.get_objects(pk)
        serializer = ImageSerializer(images, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)