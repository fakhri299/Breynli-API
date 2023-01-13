from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveAPIView,ListAPIView
from blogs.models import *
from blogs.api.serializers import *
from.qs import *
from django_filters.rest_framework import DjangoFilterBackend
from.filters import BlogFilter
from rest_framework.filters import SearchFilter


class CategoryApiView(ListAPIView):
    serializer_class=CategorySerializer
    queryset=category_list()


class BlogApiView(ListAPIView):
    serializer_class=BlogSerializer
    queryset=blog_list()
    filter_backends=[DjangoFilterBackend]
    filterset_class=BlogFilter


class BlogSearchApiView(ListAPIView):
    serializer_class=BlogSerializer
    queryset=blog_list()
    filter_backends=[SearchFilter]
    search_fields=['^title','^description','category__name','author__username']



class BlogDetailApiView(RetrieveAPIView):
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()