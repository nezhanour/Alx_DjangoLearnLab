from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = '__all__'