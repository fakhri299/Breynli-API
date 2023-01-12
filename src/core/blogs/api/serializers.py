from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blogs.models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields=['name']


class BlogSerializer(ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'