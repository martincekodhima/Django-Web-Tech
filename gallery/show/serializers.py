from .models import Image
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

class ImageSerializer(serializers.ModelSerializer):   
    photo = Base64ImageField(required=True)
    class Meta:
        model = Image
        fields = ['id', 'title', 'keyword1', 'keyword2', 'keyword3', 'photo']

class ImageDetailSerializer(serializers.ModelSerializer):   
    photo = Base64ImageField(required=True)
    class Meta:
        model = Image
        fields = ['id', 'title', 'user', 'keyword1', 'keyword2', 'keyword3', 'timestamp', 'photo']