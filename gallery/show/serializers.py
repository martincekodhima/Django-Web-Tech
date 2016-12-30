from .models import Image
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'user', 'keyword1', 'keyword2', 'keyword3', 'timestamp', 'photo']