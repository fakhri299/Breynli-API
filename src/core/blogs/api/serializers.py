from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blogs.models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields=['name']


class BlogSerializer(ModelSerializer):
    author=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Blog
        exclude=['category']