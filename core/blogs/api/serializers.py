from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blogs.models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields=['name']


class BlogSerializer(ModelSerializer):
    author=serializers.StringRelatedField(read_only=True)
    category=serializers.StringRelatedField()
    class Meta:
        model=Blog
        fields= ['title','description','body','created_date','image','author','category']


class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields=['title','subject']