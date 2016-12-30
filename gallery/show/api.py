from .models import Image
from .serializers import ImageSerializer
from django.http import Http404
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PhotoList(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializedImages = ImageSerializer(images, many=True)
        return Response(serializedImages.data)
    
    def post(self, request):
        serializer = ImageSerializer(data=request.data,files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PhotoDetail(APIView):
    def get_objects(self,pk):
        try:
            return Image.objects.get(id=pk) 
        except Image.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        images = self.get_objects(pk)
        serializedImages = ImageSerializer(images)
        return Response(serializedImages.data)
        
    def delete(self,request,pk):
        images = self.get_objects(pk)
        images.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,pk):
        images = self.get_objects(pk)
        serializer = ImageSerializer(images, data=request.data, files=request.files)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request,pk):
        images = self.get_objects(pk)
        serializer = ImageSerializer(images, data=request.data, files=request.files)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)