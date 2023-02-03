from rest_framework.generics import CreateAPIView,RetrieveAPIView,ListAPIView
from blogs.models import *
from blogs.api.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from.filters import BlogFilter
from rest_framework.filters import SearchFilter


class CategoryApiView(ListAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()


class BlogApiView(ListAPIView):
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_class=BlogFilter



class BlogDetailApiView(RetrieveAPIView):
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()


class ContactApiView(CreateAPIView):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()


