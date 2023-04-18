from rest_framework.generics import CreateAPIView,RetrieveAPIView,ListAPIView,ListCreateAPIView
from blogs.models import *
from blogs.api.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from.filters import BlogFilter




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
    


class ConsultantApiView(ListCreateAPIView):
    serializer_class=ConsultantSerializer
    queryset=Consultant.objects.all()
    


